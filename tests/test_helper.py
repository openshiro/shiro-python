import os
import vcr

def setup_vcr():
    def filter_sensitive_data(response):
        # Directly modify the response body to replace sensitive data with placeholders
        if response['body']['string']:
            original_api_key = os.environ.get("SHIRO_API_KEY").encode()
            original_prompt_id = os.environ.get("SHIRO_PROMPT_ID").encode()
            original_deployment_id = os.environ.get("SHIRO_DEPLOYMENT_ID").encode()

            # Replace sensitive data with placeholders
            response['body']['string'] = response['body']['string'].replace(original_api_key, b"<SHIRO_API_KEY>")
            response['body']['string'] = response['body']['string'].replace(original_prompt_id, b"<SHIRO_PROMPT_ID>")
            response['body']['string'] = response['body']['string'].replace(original_deployment_id, b"<SHIRO_DEPLOYMENT_ID>")
        return response

    return vcr.VCR(
        cassette_library_dir='tests/vcr_cassettes',
        record_mode='once',
        match_on=['uri', 'method'],
        filter_headers=['Authorization'],
        decode_compressed_response=True,
        before_record_response=filter_sensitive_data,
    )
