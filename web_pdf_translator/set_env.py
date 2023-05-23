environment_variables = {
    'Variables': {
        "DJANGO_SETTINGS_MODULE": "web_pdf_translator.settings",
        "SECRET_KEY": "django-insecure-i)&0u3j)4o)%c2(!g0h#vb9lbkn&l2l*dn7v*xlm7-dfalrm*8",
        "CUSTOM_AWS_ACCESS_KEY_ID": "AKIA5ILOXA2CYJHN5CGF",
        "CUSTOM_AWS_SECRET_ACCESS_KEY": "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",
        "AWS_STORAGE_BUCKET_NAME": "zappa-2g3d0h1qd",
        "function": "web-pdf-transla-dev"
    }
}

import boto3

lambda_client = boto3.client('lambda', region_name='eu-central-1')

print(lambda_client.update_function_configuration(FunctionName=environment_variables['Variables']['function'],
                                                  Environment=environment_variables))

