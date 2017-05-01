import pytest
import json
from cStringIO import StringIO
from ijson_filter.cli import do_filter


@pytest.fixture()
def test_data():
    return [
        {
            "index": 0,
            "guid": "358d07bb-8734-4ac2-aa1c-b19667fc34f7",
            "name": "Annie Sykes",
            "friends": [
                {
                    "firstname": "Marcia",
                    "lastname": "Moreno"
                },
                {
                    "firstname": "Muriel",
                    "lastname": "Church"
                },
                {
                    "firstname": "Sharpe",
                    "lastname": "Jarvis"
                },
                {
                    "firstname": "Bonita",
                    "lastname": "Robertson"
                },
                {
                    "firstname": "Ruby",
                    "lastname": "Lowery"
                },
                {
                    "firstname": "Ortega",
                    "lastname": "Kinney"
                },
                {
                    "firstname": "Gaines",
                    "lastname": "Cash"
                },
                {
                    "firstname": "Tisha",
                    "lastname": "Snider"
                },
                {
                    "firstname": "Christi",
                    "lastname": "Mathis"
                }
            ]
        },
        {
            "index": 1,
            "guid": "d207a3bc-5ba5-439f-be18-8f8597c79fa2",
            "name": "Kimberley Black",
            "friends": [
                {
                    "firstname": "Norman",
                    "lastname": "Dunlap"
                },
                {
                    "firstname": "Rhodes",
                    "lastname": "Patterson"
                },
                {
                    "firstname": "Moody",
                    "lastname": "Shelton"
                }
            ]
        },
        {
            "index": 2,
            "guid": "97e14441-d16b-4552-a0ca-f1b3dd0e95a8",
            "name": "Compton Norton",
            "friends": [
                {
                    "firstname": "Hallie",
                    "lastname": "Whitley"
                },
                {
                    "firstname": "Whitney",
                    "lastname": "Montoya"
                },
                {
                    "firstname": "Colleen",
                    "lastname": "Hardy"
                },
                {
                    "firstname": "Alexandria",
                    "lastname": "Ball"
                },
                {
                    "firstname": "Saundra",
                    "lastname": "Porter"
                },
                {
                    "firstname": "Sexton",
                    "lastname": "Downs"
                },
                {
                    "firstname": "Carmela",
                    "lastname": "Swanson"
                },
                {
                    "firstname": "Magdalena",
                    "lastname": "Roth"
                },
                {
                    "firstname": "West",
                    "lastname": "Roach"
                },
                {
                    "firstname": "Celeste",
                    "lastname": "Tyson"
                }
            ]
        },
        {
            "index": 3,
            "guid": "1638de5c-127f-4302-a1b5-ac5584fe087c",
            "name": "Burks Anthony",
            "friends": [
                {
                    "firstname": "Jerry",
                    "lastname": "Harrison"
                },
                {
                    "firstname": "Abbott",
                    "lastname": "Olsen"
                },
                {
                    "firstname": "Eva",
                    "lastname": "Larson"
                }
            ]
        },
        {
            "index": 4,
            "guid": "2ece3a50-6974-495a-8de5-433664c3df19",
            "name": "Boyd Watson",
            "friends": [
                {
                    "firstname": "Liliana",
                    "lastname": "Rollins"
                },
                {
                    "firstname": "Ray",
                    "lastname": "Warren"
                }
            ]
        },
        {
            "index": 5,
            "guid": "ea9da7d8-4dcd-436e-ae50-0d98a4033724",
            "name": "Young Walters",
            "friends": [
                {
                    "firstname": "Torres",
                    "lastname": "Mclaughlin"
                },
                {
                    "firstname": "Charmaine",
                    "lastname": "Morton"
                },
                {
                    "firstname": "Bray",
                    "lastname": "Gray"
                },
                {
                    "firstname": "Erickson",
                    "lastname": "Byers"
                },
                {
                    "firstname": "Angeline",
                    "lastname": "Odonnell"
                },
                {
                    "firstname": "Goldie",
                    "lastname": "Sheppard"
                },
                {
                    "firstname": "Henry",
                    "lastname": "Montgomery"
                },
                {
                    "firstname": "Marisol",
                    "lastname": "Henry"
                },
                {
                    "firstname": "Stuart",
                    "lastname": "Sutton"
                }
            ]
        }
    ]


@pytest.fixture()
def test_data_json(test_data):
    return json.dumps(test_data)


def call_cli(inp, filters):
    out = StringIO()
    do_filter(StringIO(inp), out, filters, False)
    return json.loads(out.getvalue())
