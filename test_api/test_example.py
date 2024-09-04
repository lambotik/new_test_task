import allure
import pytest

from test_api.checking import Checking
from test_api.request import API


@allure.epic('API.')
class TestApi:
    @allure.suite('GET')
    @allure.title('test_posts_keys')
    def test_posts_keys(self):
        response = API.get_posts()
        Checking.check_status_code(response, 200)
        Checking.check_json_all_keys(response, ['userId', 'id', 'title', 'body'])

    @allure.suite('GET')
    @allure.title('test_posts_by_id')
    def test_posts_by_id(self):
        response = API.get_posts_by_id(1)
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'id', 1)
        Checking.check_json_value(response, 'userId', 1)

    @allure.suite('POST')
    @allure.title('test_post_creating_resource')
    def test_post_creating_resource(self):
        body = {'title': 'foo',
                'body': 'bar',
                'userId': 1}
        response = API.post_creating_resource(body=body)
        Checking.check_status_code(response, 201)
        Checking.check_json_keys(response, ['title', 'body', 'userId', 'id'])
        Checking.check_json_value(response, 'title', body['title'])
        Checking.check_json_value(response, 'body', body['body'])
        Checking.check_json_value(response, 'userId', body['userId'])

    @allure.suite('PUT')
    @pytest.mark.parametrize('set_id', (1, 10, 100, 1000, '99', -1))
    def test_updating_resource(self, set_id):
        allure.dynamic.title(f'test_updating_resource_by_id_{set_id}')
        body = {'id': set_id,
                'title': 'foo',
                'body': 'bar',
                'userId': 1}
        response = API.put_updating_resource(
            body=body,
            set_id=set_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_value(response, 'id', set_id)

    @allure.suite('DELETE')
    @pytest.mark.parametrize('set_id', (1, 10, 100, 1000, '99', -1))
    @pytest.mark.xfail(reason="Some tests should fail due to invalid data.")
    def test_delete_resource(self, set_id):
        allure.dynamic.title(f'test_delete_resource_by_id_{set_id}')
        response = API.delete_resource(set_id=set_id)
        Checking.check_status_code(response, 200)
        assert response.text == '{}'

    @allure.suite('DELETE')
    @pytest.mark.parametrize('set_id', (1, 10, 100, 1000, '99', -1))
    @pytest.mark.xfail(reason="Some tests should fail due to invalid data.")
    def test_delete_resource(self, set_id):
        allure.dynamic.title(f'test_delete_resource_by_id_{set_id}_and_check_it')
        response = API.delete_resource(set_id=set_id)
        Checking.check_status_code(response, 200)
        assert response.text == '{}'
        response = API.get_posts_by_id(set_id)
        Checking.check_status_code(response, 404)
