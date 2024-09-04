import requests


class HttpMethods:
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    cookie = ''

    @staticmethod
    def get(url, body=None, token=None):
        """
        :param url:
        :param body:
        :param token:
        :return: requests.models.Response
        """
        response = requests.get(
            url=url,
            headers=HttpMethods.headers | {'Authorization': f'{token}'},
            cookies=HttpMethods.cookie,
            json=body)
        return response

    @staticmethod
    def post(url, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json
        :return: requests.models.Response
        """
        response = requests.post(
            url=url,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        return response

    @staticmethod
    def put(url, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json
        :return: requests.models.Response
        """
        response = requests.put(
            url=url,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        return response

    @staticmethod
    def patch(url, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json
        :return: requests.models.Response
        """
        response = requests.patch(
            url=url,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        return response

    @staticmethod
    def delete(url, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json:
        :return: requests.models.Response
        """
        response = requests.delete(
            url=url,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        return response
