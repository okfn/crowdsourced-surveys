# POST on /forms

api_test_form = {
    "name": "[test] API wrapper",
    "type": "report",
    "description": "API test"
}

api_test_stage = {
    "label": "Some label",
    "priority": 0,
    "required": False,
    "type": "post",
    "show_when_published": True,
    "task_is_internal_only": False,
    "is_public": True,
    "form_id": None,
    "formId": None,
}

api_test_attributes = [
    {
        "cardinality": 0,
        "input": "text",
        "label": "Title",
        "priority": 1,
        "required": True,
        "type": "title",
    },
    {
        "cardinality": 0,
        "input": "text",
        "label": "Description",
        "priority": 2,
        "required": True,
        "type": "description",
    }
]


tanzania_schools_form = {
    "color": None,
    "require_approval": True,
    "name": "Schools in Tanzania",
    "description": "Mapping all the schools in Tanzania",
    "type": "report"
}
tanzania_schools_stage = {
    "label": "Post",
    "priority": 0,
    "required": False,
    "type": "post",
    "show_when_published": True,
    "task_is_internal_only": False,
    "is_public": True,
    "form_id": None,
    "formId": None,
}
tanzania_schools_attributes = [
    {
        "cardinality": 0,
        "input": "text",
        "label": "Name of school",
        "priority": 1,
        "required": True,
        "type": "title",
        "response_private": True
    },
    {
        "cardinality": 0,
        "input": "text",
        "label": "Name of ward",
        "priority": 2,
        "required": True,
        "type": "description",
        "response_private": True
    },
    {
        "required": True,
        "options": [
            "Pre-school",
            "Primary school",
            "Secondary school",
            "High school"
        ],
        "config": {

        },
        "priority": 3,
        "label": "Type of school",
        "type": "varchar",
        "input": "checkbox",
        "cardinality": 0,
        "description": "Allows the user to choose one or more of a predefined set of options.",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    },
    {
        "required": True,
        "options": [

        ],
        "config": {

        },
        "priority": 4,
        "label": "Location",
        "type": "point",
        "input": "location",
        "description": "A geographic location chosen via a map",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    },
    {
        "required": False,
        "options": [

        ],
        "config": {

        },
        "priority": 5,
        "label": "School address",
        "type": "text",
        "input": "textarea",
        "description": "Multiple sentences or paragraphs",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    },
    {
        "required": False,
        "options": [

        ],
        "config": {
            "hasCaption": True
        },
        "priority": 6,
        "label": "Photo of school",
        "type": "media",
        "input": "upload",
        "description": "Allows image(s) to be uploaded to the post",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    },
    {
        "required": False,
        "options": [

        ],
        "config": {

        },
        "priority": 7,
        "label": "Additional notes",
        "type": "text",
        "input": "textarea",
        "description": "Multiple sentences or paragraphs",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    },
    {
        "required": False,
        "options": [

        ],
        "config": {

        },
        "priority": 8,
        "label": "Feedback",
        "type": "text",
        "input": "textarea",
        "description": "Multiple sentences or paragraphs",
        "response_private": True,
        "form_stage_id": "interim_id_2"
    }
]

tanzania_schools = """
{
  "color":null,
  "require_approval":true,
  "everyone_can_create":true,
  "tasks":[
    {
      "label":"Post",
      "priority":0,
      "required":false,
      "type":"post",
      "show_when_published":true,
      "task_is_internal_only":false,
      "attributes":[
        {
          "cardinality":0,
          "input":"text",
          "label":"Name of school",
          "priority":1,
          "required":true,
          "type":"title",
          "options":[

          ],
          "config":{

          },
          "form_stage_id":"interim_id_0",
          "response_private":true
        },
        {
          "cardinality":0,
          "input":"text",
          "label":"Name of ward",
          "priority":2,
          "required":true,
          "type":"description",
          "options":[

          ],
          "config":{

          },
          "form_stage_id":"interim_id_1",
          "response_private":true
        },
        {
          "required":true,
          "options":[
            "Pre-school",
            "Primary school",
            "Secondary school",
            "High school"
          ],
          "config":{

          },
          "priority":3,
          "label":"Type of school",
          "type":"varchar",
          "input":"checkbox",
          "cardinality":0,
          "description":"Allows the user to choose one or more of a predefined set of options.",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        },
        {
          "required":true,
          "options":[

          ],
          "config":{

          },
          "priority":4,
          "label":"Location",
          "type":"point",
          "input":"location",
          "description":"A geographic location chosen via a map",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        },
        {
          "required":false,
          "options":[

          ],
          "config":{

          },
          "priority":5,
          "label":"School address",
          "type":"text",
          "input":"textarea",
          "description":"Multiple sentences or paragraphs",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        },
        {
          "required":false,
          "options":[

          ],
          "config":{
            "hasCaption":true
          },
          "priority":6,
          "label":"Photo of school",
          "type":"media",
          "input":"upload",
          "description":"Allows image(s) to be uploaded to the post",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        },
        {
          "required":false,
          "options":[

          ],
          "config":{

          },
          "priority":7,
          "label":"Additional notes",
          "type":"text",
          "input":"textarea",
          "description":"Multiple sentences or paragraphs",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        },
        {
          "required":false,
          "options":[

          ],
          "config":{

          },
          "priority":8,
          "label":"Feedback",
          "type":"text",
          "input":"textarea",
          "description":"Multiple sentences or paragraphs",
          "response_private":true,
          "form_stage_id":"interim_id_2"
        }
      ],
      "is_public":true,
      "id":"interim_id_2"
    }
  ],
  "name":"Schools in Tanzania",
  "description":"Mapping all the schools in Tanzania"
}
"""

