import os
import click
import requests
from utils.api import ApiWrapper
from fixtures import forms

api = ApiWrapper()

# api.get_user()
# api.toggle_private()
# api.create_survey(tanzania_survey)


@click.group()
def cli():
    pass


@click.command()
@click.option('--form', '-f', help='Name of the form (fixture) to upload')
def send_form(form):
    form_name = form
    form_payload = getattr(forms, '%s_form' % form_name, False)

    if not form_payload:
        click.echo(click.style('Form %s not found!' % form_name, fg='red'))
    else:
        click.echo('Submitting form %s... ' % form_name, nl=False)
        form = api.create_form(data=form_payload, verbose=False)

        if not form:
            click.echo(click.style('failed!', fg='red'))
        else:
            click.echo('done (id %s).' % form['id'])

        click.echo('Adding stage to form %s... ' % form['id'], nl=False)
        stage_payload = getattr(forms, '%s_stage' % form_name, {})
        stage = api.create_stage(form['id'], data=stage_payload, verbose=False)
        if not stage:
            click.echo(click.style('failed!', fg='red'))
        else:
            click.echo('done (id %s).' % stage['id'])

        click.echo('Adding attributes to form %s: ' % form['id'], nl=False)
        attributes_payload = getattr(forms, '%s_attributes' % form_name, [])
        for payload in attributes_payload:
            attribute = api.create_attribute(
                form_id=form['id'],
                stage_id=stage['id'],
                data=payload,
                verbose=False
            )
            if not attribute:
                click.echo(click.style('%s ' % payload['label'], fg='red'), nl=False)
            else:
                click.echo(click.style('%s ' % payload['label'], fg='green'), nl=False)
        print()


@click.command()
@click.option('--id', '-i', help='Name of the survey to upload')
def delete_form(id):
    click.echo('Deleting form %s... ' % id, nl=False)
    res = api.delete_form(id)
    if not res:
        click.echo(click.style('failed!', fg='red'))
    else:
        click.echo('done.')


@click.command()
@click.option('--form', help='Form ID to submit for')
@click.option('--answer', help='Answer payload')
def send_answer(form, answer):
    click.echo('Submitting answer to form %s' % form)
    click.echo('Answer payload is %s' % answer)
    # print('Answer is %s' % answer)


@click.command()
@click.option('-a', help='Test authentication', is_flag=True)
@click.option('-p', help='Ping test', is_flag=True)
@click.option('-t', help='Time to API and back', is_flag=True)
@click.option('-e', help='Print env vars (paged)', is_flag=True)
def test(a, p, t, e):
    if not any((a, p, t, e)):
        click.echo('No test specified, defaulting to ping test')
        p = True

    if a:
        if api.get_token():
            click.echo(click.style('Token OK', fg='green'))
        else:
            click.echo(click.style('Cannot get token', fg='red'))
    if p:
        test = api.test()
        if test.status_code == requests.codes.ok:
            click.echo(click.style('API is online', fg='green'))
        else:
            click.echo(click.style('API is offline', fg='red'))
    if t:
        test = api.test()
        click.echo('Time elapsed: %s' % test.elapsed)
    if e:
        click.echo_via_pager('\n'.join('%s=%s' % (key, value)
                                       for key, value in os.environ.items()))


cli.add_command(send_form)
cli.add_command(send_answer)
cli.add_command(delete_form)
cli.add_command(test)


if __name__ == '__main__':
    cli()
