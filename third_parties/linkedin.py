import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url, mock: bool = False):
    ''' This function scrapes information from linkedin profile'''
    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/amitjathardev/9fe9609598cf215bfd96f4731260c087/raw/77d05be4916fe8733d0935ac63b9149d7f4114c1/amitjathar-dev.jason"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        #api_key = 'LtHUVULf_o-B9u1VVb0VMg'
        headers = {'Authorization': f'Bearer {os.environ.get("proxycurl_api_key")}'}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        linkedin_profile_url = 'https://www.linkedin.com/in/amitjathar99/'

        response = requests.get(api_endpoint,
                                params={'url': linkedin_profile_url},
                                headers=headers,
                                timeout=10)

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ("people_also_viewed", "certifications")
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/amitjathar99/",
            mock=True
        )
    )
