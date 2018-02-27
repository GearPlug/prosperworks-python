import requests
from prosperworks import exceptions


class Client(object):
    BASE = 'https://api.prosperworks.com/developer_api/'

    def __init__(self, api_key, email, api_version='v1'):
        self.api_key = api_key
        self.api_version = api_version
        self.email = email
        self.base_url = self.BASE + self.api_version + '/'

    # Account, hace referencia a la organizacion que maneja
    # la cuenta de Prosperworks
    def get_account_info(self):
        """
        Return basic information about account
        Returns:

        """
        endpoint = 'account'
        return self._get(endpoint)

    def get_users_list(self):
        """
        Return all users info
        Returns:

        """
        # search filter
        querystring = {"page_size": "200"}
        endpoint = "users/search"
        return self._post(endpoint, params=querystring)

    def get_user(self, _id):
        """
        Return info of specific user
        Args:
            _id: id of user

        Returns:

        """
        endpoint = "users/{}".format(str(_id))
        return self._get(endpoint)

    # Leads
    def get_leads_list(self):
        """
        Return list of leads order by date of creation
        Returns:

        """
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        endpoint = "leads/search"
        return self._post(endpoint, params=querystring)

    def get_lead_by_id(self, _id):
        """
        Return lead info
        Args:
            _id: id of lead to get

        Returns:

        """
        endpoint = "leads/{}".format(str(_id))
        return self._get(endpoint)

    def get_lead_by_email(self, email):
        """
        Search leads by email
        Args:
            email: search param

        Returns:

        """
        endpoint = "leads/search"
        querystring = {
            "emails": "{}".format(email)
        }
        return self._post(endpoint, params=querystring)

    def get_lead_by_full_name(self, full_name):
        """
        Search leads by full name
        Args:
            full_name: search param

        Returns:

        """
        endpoint = "leads/search"
        querystring = {
            "name": "{}".format(full_name)
        }
        return self._post(endpoint, params=querystring)

    def get_lead_by_phone_number(self, phone):
        """
        Search for leads by phone number
        Args:
            phone: search param

        Returns:

        """
        endpoint = "leads/search"
        querystring = {
            "phone_number": "{}".format(phone)
        }
        return self._post(endpoint, params=querystring)

    def create_new_lead(self, **kwargs):
        """
        Return dict with info of the new lead created
        look for id and date_created inside that dict
        Args:
            **kwargs: dict with the require info for creating
            a new lead:
                {
                    "name":"My Lead",
                    "email": {
                        "email":"mylead@noemail.com",
                        "category":"work"
                    },
                    "phone_numbers": [
                        {
                            "number":"415-123-45678",
                            "category":"mobile"
                        }],
                    "custom_fields": [
                    {
                        "custom_field_definition_id": 100764,
                        "value": "Text fields are 255 chars or less!"
                    },
                    {
                        "custom_field_definition_id": 103481,
                        "value": "Text area fields can have long text content"
                    }
                    ],
                    "customer_source_id":331242
                }
            In the above example, custom_fields is optional

        Returns:
        """
        endpoint = "leads"
        return self._post(endpoint, json=kwargs)

    # People
    def get_person_by_id(self, _id):
        """
        Return person information
        Args:
            _id: id of person

        Returns:

        """
        endpoint = "people/{}".format(str(_id))
        return self._get(endpoint)

    def get_person_by_email(self, email):
        """
        Search person by email
        Args:
            email: search param

        Returns:

        """
        endpoint = "people/fetch_by_email"
        querystring = {
            "email": "{}".format(email)
        }
        return self._post(endpoint, params=querystring)

    def get_person_by_full_name(self, full_name):
        """
        Search person by full name
        Args:
            full_name: search param

        Returns:

        """
        endpoint = "people/search"
        querystring = {
            "name": "{}".format(full_name)
        }
        return self._post(endpoint, params=querystring)

    def get_person_by_phone_number(self, phone):
        """
        Search for person by phone number
        Args:
            phone: search param

        Returns:

        """
        endpoint = "people/search"
        querystring = {
            "phone_number": "{}".format(phone)
        }
        return self._post(endpoint, params=querystring)

    def get_list_of_people(self):
        """
        Return list of people
        Returns:

        """
        endpoint = "people/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_person(self, **kwargs):
        """
        Return dict with info of the new comapny created
        Args:
            **kwargs:dict with the require info for creating
            a new person:
                {
                  "name":"My Contact",
                  "emails": [
                    {
                    "email":"mycontact_1233@noemail.com",
                    "category":"work"
                    }
                  ],
                  "phone_numbers": [
                    {
                    "number":"415-123-45678",
                    "category":"mobile"
                    }
                  ]
                }
        Returns:

        """
        endpoint = "people"
        return self._post(endpoint, json=kwargs)

    # Companies
    def get_company_by_id(self, _id):
        """
        Returns company info by id
        Args:
            _id: id of company

        Returns:

        """
        endpoint = "companies/{}".format(str(_id))
        return self._get(endpoint)

    def get_company_by_full_name(self, full_name):
        """
        Search company by full name
        Args:
            full_name: search param

        Returns:

        """
        endpoint = "companies/search"
        querystring = {
            "name": "{}".format(full_name)
        }
        return self._post(endpoint, params=querystring)

    def get_company_by_phone_number(self, phone):
        """
        Search for company by phone number
        Args:
            phone: search param

        Returns:

        """
        endpoint = "companies/search"
        querystring = {
            "phone_number": "{}".format(phone)
        }
        return self._post(endpoint, params=querystring)

    def get_list_of_company(self):
        """
        Return list of companies
        Returns:

        """
        endpoint = "companies/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_company(self, **kwargs):
        """
        Return dict with info of the new company created
        Args:
            **kwargs:dict with the require info for creating
            a new person:
                {
                  "name":"Demo Company",
                  "address": {
                    "street":"123 Main St",
                    "city": "San Francisco",
                    "state":"CA",
                    "postal_code": "94105"
                  },
                  "email_domain":"democompany.com",
                  "details":"This is a demo company",
                  "phone_numbers": [
                    {
                    "number":"415-123-45678",
                    "category":"work"
                    }
                  ]
                }
        Returns:
        """
        endpoint = "companies"
        return self._post(endpoint, json=kwargs)

    # Opportunities
    def get_opportunity_by_id(self, _id):
        """
        Returns opportunity info by id
        Args:
            _id: id of opportunity

        Returns:

        """
        endpoint = "opportunities/{}".format(str(_id))
        return self._get(endpoint)

    def get_opportunity_by_full_name(self, full_name):
        """
        Search opportunity by full name
        Args:
            full_name: search param

        Returns:

        """
        endpoint = "opportunities/search"
        querystring = {
            "name": "{}".format(full_name)
        }
        return self._post(endpoint, params=querystring)

    def get_list_of_opportunities(self):
        """
        Return list of companies
        Returns:

        """
        endpoint = "opportunities/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_opportunity(self, **kwargs):
        """
        Return dict with info of the new opportunity created
        Args:
            **kwargs:dict with the require info for creating
            a new person:
                {
                  "name": "New Demo Opportunity",
                  "primary_contact_id": 27140359,
                  "customer_source_id":331242
                }
        Returns:
        """
        endpoint = "opportunities"
        return self._post(endpoint, json=kwargs)

    # Projects
    def get_project_by_id(self, _id):
        """
        Returns project info by id
        Args:
            _id: id of company

        Returns:

        """
        endpoint = "projects/{}".format(str(_id))
        return self._get(endpoint)

    def get_list_of_project(self):
        """
        Return list of projects
        Returns:

        """
        endpoint = "projects/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_project(self, **kwargs):
        """
        Return dict with info of the new project created
        Args:
            **kwargs:dict with the require info for creating
            a new project:
                {
                  "name":"New Demo Project"
                }
        Returns:
        """
        endpoint = "projects"
        return self._post(endpoint, json=kwargs)

    # Tasks
    def get_task_by_id(self, _id):
        """
        Returns task info by id
        Args:
            _id: id of task

        Returns:

        """
        endpoint = "tasks/{}".format(str(_id))
        return self._get(endpoint)

    def get_list_of_tasks(self):
        """
        Return list of tasks
        Returns:

        """
        endpoint = "tasks/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_task(self, **kwargs):
        """
        Return dict with info of the new task created
        Args:
            **kwargs:dict with the require info for creating
            a new task:
                {
                    "name": "Demo task",
                    "related_resource": {
                        "id": 144296,
                        "type": "project"
                    },
                    "due_date": 1496799000,
                    "reminder_date": null,
                    "priority": "None",
                    "status": "Open",
                    "details": "This needs to be done!",
                    "custom_fields": []
                }
        Returns:
        """
        endpoint = "tasks"
        return self._post(endpoint, json=kwargs)

    # Activities
    def get_activities_by_id(self, _id):
        """
        Returns task info by id
        Args:
            _id: id of task

        Returns:

        """
        endpoint = "activities/{}".format(str(_id))
        return self._get(endpoint)

    def get_list_of_activities(self):
        """
        Return list of tasks
        Returns:

        """
        endpoint = "activities/search"
        querystring = {
            "sort_by": "date_created",
            "page_size": "200",
            "sort_direction": "asc"
        }
        return self._post(endpoint, params=querystring)

    def create_new_activities(self, **kwargs):
        """
        Return dict with info of the new task created
        Args:
            **kwargs:dict with the require info for creating
            a new task:
                {
                      "parent": {
                        "type": "person",
                        "id": 27140359
                      },
                      "type": {
                        "category": "user",
                        "id": 0
                      },
                      "details": "This is the description of this note"

                    }
        Returns:
        """
        endpoint = "activities"
        return self._post(endpoint, json=kwargs)

    # Subscriptions (Webhooks)
    def get_list_of_subscriptions(self):
        """
        Return list of tasks
        Returns:

        """
        endpoint = "webhooks"
        return self._get(endpoint)

    def create_new_subscription(self, body):
        """
        Return dict with info of the new task created
        "event" = "new" | "update" | "delete"
        "type" = "lead" | "person" | "company" | "deal" | "project" | "task"
        Args:
            **kwargs:dict with the require info for creating
            a new subscription:
                {
                  "target": "https://your.endpoint.here",
                  "type": "lead",
                  "event": "update",
                  "secret": {
                    "secret": "hook_source",
                    "key": "prosperworks_notifications"
                  }
                }
        Returns:
        """
        endpoint = "webhooks"
        return self._post(endpoint, json=body)

    def delete_subscription(self, _id):
        """
        Delete subscription by id
        Args:
            _id: id of subscription

        Returns:

        """
        endpoint = "webhooks/{}".format(str(_id))
        return self._delete(endpoint)

    def _get(self, endpoint, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def _put(self, endpoint, **kwargs):
        return self._request('PUT', endpoint, **kwargs)

    def _patch(self, endpoint, **kwargs):
        return self._request('PATCH', endpoint, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def _request(self, method, endpoint, **kwargs):
        _headers = {
            'X-PW-AccessToken': "{}".format(self.api_key),
            'X-PW-Application': "developer_api",
            'X-PW-UserEmail': "{}".format(self.email),
            'Content-Type': "application/json"
        }
        url = self.base_url + endpoint
        return self._parse(requests.request(method, url, headers=_headers, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        if status_code in (200, 201, 202):
            return r
        elif status_code == 204:
            return None
        elif status_code == 400:
            raise exceptions.BadRequest(r)
        elif status_code == 401:
            raise exceptions.Unauthorized(r)
        elif status_code == 403:
            raise exceptions.Forbidden(r)
        elif status_code == 404:
            raise exceptions.NotFound(r)
        elif status_code == 405:
            raise exceptions.MethodNotAllowed(r)
        elif status_code == 406:
            raise exceptions.NotAcceptable(r)
        elif status_code == 409:
            raise exceptions.Conflict(r)
        elif status_code == 410:
            raise exceptions.Gone(r)
        elif status_code == 411:
            raise exceptions.LengthRequired(r)
        elif status_code == 412:
            raise exceptions.PreconditionFailed(r)
        elif status_code == 413:
            raise exceptions.RequestEntityTooLarge(r)
        elif status_code == 415:
            raise exceptions.UnsupportedMediaType(r)
        elif status_code == 416:
            raise exceptions.RequestedRangeNotSatisfiable(r)
        elif status_code == 422:
            raise exceptions.UnprocessableEntity(r)
        elif status_code == 429:
            raise exceptions.TooManyRequests(r)
        elif status_code == 500:
            raise exceptions.InternalServerError(r)
        elif status_code == 501:
            raise exceptions.NotImplemented(r)
        elif status_code == 503:
            raise exceptions.ServiceUnavailable(r)
        elif status_code == 504:
            raise exceptions.GatewayTimeout(r)
        elif status_code == 507:
            raise exceptions.InsufficientStorage(r)
        elif status_code == 509:
            raise exceptions.BandwidthLimitExceeded(r)
        else:
            raise exceptions.UnknownError(r)