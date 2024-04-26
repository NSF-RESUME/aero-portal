
from django.apps import AppConfig
from dsaas_portal import checks
from dsaas_portal import fields

class Dsaasportal(AppConfig):
    name = 'DSaaS'



SEARCH_INDEXES = {
    "dsaas_portal": {
        "uuid": "ef085c4b-7ce8-4955-b22f-8c907b690abb",
        "name": "DSaaS",
        "template_override_dir": "dsaas_portal",
        "facets": [
            {
                'name': 'Name',
                'field_name': 'name'
            },
            {
                'name': 'URL',
                'field_name': 'url'
            },
            {
                'name': 'Description',
                'field_name': 'description',
            },
            {
                'name': 'Email',
                'field_name': 'email',
            },
            {
                'name': 'Tags',
                'field_name': 'tags',
            },
            {
                'name': 'Source Name',
                'field_name': 'source',
            },
            {
                'name': 'Source ID',
                'field_name': 'source_id',
            },
            {
                'name': 'Version',
                'field_name': 'version'
            },
            {
                'name': 'Checksum',
                'field_name': 'checksum'
            },
            {
                'name': 'File Size',
                'field_name': 'file_size'
            },
            {
                'name': 'Date Created',
                'field_name': 'date_created'
            }
        ],
        "fields": [
            # Calls a function with your search record as a parameter
            ("title", fields.title),
            ("globus_app_link", fields.globus_app_link),
            ("https_url", fields.https_url),
            ("copy_to_clipboard_link", fields.https_url),
        ],
    }
}
