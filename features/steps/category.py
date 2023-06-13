import requests
from behave import given, when, then

@given('I have category {category_id}')
def step_given_category_id(context, category_id):
    context.category_id = category_id


@when('I request the category details with "{params}"')
def step_when_requesting_details(context, params):
    uri = get_category_details_uri(context, params)
    context.response = requests.get(uri)


@then('It should return json with the following details')
def step_should_return_the_following_details(context):
    response = context.response.json()
    for row in context.table:
        field = row['Field']
        expected_value = row['Value']
        actual_value = response.get(field)
        assert str(actual_value) == str(expected_value), f'Expected {field} to be "{expected_value}", got {actual_value}'


@then('It should return json with the following category promotions')
def step_should_have_the_following_promotion(context):
    response = context.response.json()
    promotions = response.get("Promotions")
    for row in context.table:
        promotion = list(filter(lambda p: p['Name'] == row['Name'], promotions))[0]
        assert promotion is not None, f'Expected promotion name {row["Name"]}, found none'
        assert row['Description'] in promotion["Description"], f'Expected promotion description {row["Description"]}, got {promotion["Description"]}'


def get_category_details_uri(context, params: None):
    uri = f'{context.base_url}/v1/Categories/{context.category_id}/details.json'
    if params is not None:
        uri += f'?{params}'
    return uri
