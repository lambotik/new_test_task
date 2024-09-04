import allure

from test_api.http_methods import HttpMethods


class API:
    base_url = 'https://jsonplaceholder.typicode.com'

    @staticmethod
    def get_posts():
        get_resource = f'/posts'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /posts'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_posts_by_id(set_id):
        get_resource = f'/posts/{set_id}'
        url = API.base_url + get_resource
        response = HttpMethods.get(url=url)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def post_creating_resource(body: dict):
        post_resource = f'/posts'
        url = API.base_url + post_resource
        response = HttpMethods.post(url=url, body=body)
        with allure.step('Endpoint: /posts'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {body}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def put_updating_resource(body: dict, set_id):
        put_resource = f'/posts/{set_id}'
        url = API.base_url + put_resource
        response = HttpMethods.put(url=url, body=body)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {body}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def delete_resource(set_id):
        delete_resource = f'/posts/{set_id}'
        url = API.base_url + delete_resource
        response = HttpMethods.delete(url=url)
        with allure.step(f'Endpoint: /posts/{set_id}'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response
