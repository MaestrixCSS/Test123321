def parse(response: dict) -> list[str]:
    people_list = response.get("people", {}).get("result", [])

    return [person["login"] for person in people_list if "login" in person]


response = {
    "people": {
        "result": [
            {
                "url": "https://staff.yandex-team.ru/robot-support-taxi",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=0/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Frobot-support-taxi/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Frobot-support-taxi"
                ],
                "layer": "people",
                "id": "robot-support-taxi",
                "title": "Робот Саптеха",
                "staff_id": 25462,
                "uid": "1120000000050978",
                "login": "robot-support-taxi",
                "name": {
                    "first": "Робот",
                    "last": "Саптеха",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": True,
                "is_memorial": False,
                "staff_agreement": False,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/kefiro4naya",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=1/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fkefiro4naya/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fkefiro4naya"
                ],
                "layer": "people",
                "id": "kefiro4naya",
                "title": "Ярослав Тихонович",
                "staff_id": 523257,
                "uid": "1120000000935110",
                "login": "kefiro4naya",
                "name": {
                    "first": "Ярослав",
                    "last": "Тихонович",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": False,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/zolmasha",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=2/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fzolmasha/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fzolmasha"
                ],
                "layer": "people",
                "id": "zolmasha",
                "title": "Мария Золотогорная",
                "staff_id": 514979,
                "uid": "1120000000921784",
                "login": "zolmasha",
                "name": {
                    "first": "Мария",
                    "last": "Золотогорная",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/proudnika",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=3/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fproudnika/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fproudnika"
                ],
                "layer": "people",
                "id": "proudnika",
                "title": "Вероника Дрягалова",
                "staff_id": 420743,
                "uid": "1120000000635721",
                "login": "proudnika",
                "name": {
                    "first": "Вероника",
                    "last": "Дрягалова",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/nikos13",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=4/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fnikos13/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fnikos13"
                ],
                "layer": "people",
                "id": "nikos13",
                "title": "Никита Тимонин",
                "staff_id": 355838,
                "uid": "1120000000482996",
                "login": "nikos13",
                "name": {
                    "first": "Никита",
                    "last": "Тимонин",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/lyle",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=5/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Flyle/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Flyle"
                ],
                "layer": "people",
                "id": "lyle",
                "title": "Тамерлан Саркитов",
                "staff_id": 82208,
                "uid": "1120000000225353",
                "login": "lyle",
                "name": {
                    "first": "Тамерлан",
                    "last": "Саркитов",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "yandex",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/robot-suptech-eda",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=6/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Frobot-suptech-eda/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Frobot-suptech-eda"
                ],
                "layer": "people",
                "id": "robot-suptech-eda",
                "title": "Саптеховец Едовской",
                "staff_id": 394950,
                "uid": "1120000000596381",
                "login": "robot-suptech-eda",
                "name": {
                    "first": "Саптеховец",
                    "last": "Едовской",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": True,
                "is_memorial": False,
                "staff_agreement": False,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/s-nikitenko",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=7/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fs-nikitenko/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fs-nikitenko"
                ],
                "layer": "people",
                "id": "s-nikitenko",
                "title": "Светлана Никитенко",
                "staff_id": 33168,
                "uid": "1120000000077819",
                "login": "s-nikitenko",
                "name": {
                    "first": "Светлана",
                    "last": "Никитенко",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": False,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/v-a-babenko",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=8/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fv-a-babenko/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fv-a-babenko"
                ],
                "layer": "people",
                "id": "v-a-babenko",
                "title": "Владислав Бабенко",
                "staff_id": 77305,
                "uid": "1120000000203815",
                "login": "v-a-babenko",
                "name": {
                    "first": "Владислав",
                    "last": "Бабенко",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "external",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": []
            },
            {
                "url": "https://staff.yandex-team.ru/vtitoff",
                "click_urls": [
                    "//clck.yandex.ru/click/dtype=SAAS/p=9/saas_url=https%3A%2F%2Fstaff.yandex-team.ru%2Fvtitoff/robot=0/r=%25D0%25A1%25D0%25B0%25D0%25BF%25D1%2582%25D0%25B5%25D1%2585/service=intrasearch-people/kps=83933/uid=is1120000000690263/yandexuid=is1120000000690263/reqid=1752599193777082-18338190438510340352-saas-searchproxy-stable-vla-18-SAAS-intrasearch-people/raId=95F6B9F318A5F4F4/slots=1317008,0,96;1308584,0,61;1272065,0,51;1312773,0,56;1211160,0,83/how=rlv/*data=url%3Dhttps%3A%2F%2Fstaff.yandex-team.ru%2Fvtitoff"
                ],
                "layer": "people",
                "id": "vtitoff",
                "title": "Владислав Титов",
                "staff_id": 35759,
                "uid": "1120000000086183",
                "login": "vtitoff",
                "name": {
                    "first": "Владислав",
                    "last": "Титов",
                    "middle": ""
                },
                "is_dismissed": False,
                "affiliation": "yandex",
                "is_robot": False,
                "is_memorial": False,
                "staff_agreement": True,
                "person_skills": [
                    "Python",
                    "PostgreSQL",
                    "SQL",
                    "YQL",
                    "FastAPI",
                    "Django",
                    "Redis",
                    "Docker",
                    "AIOHTTP",
                    "aiogram",
                    "Asyncio",
                    "MongoDB",
                    "YDB"
                ]
            }
        ],
        "pagination": {
            "page": 0,
            "per_page": 10,
            "pages": 64,
            "count": 639
        }
    }
}

if __name__ == "__main__":
    logins = parse(response)
print(logins)
