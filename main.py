#!/usr/bin/env python3

from pydriller import RepositoryMining
from datetime import datetime
import json


def get_relevant_commits(repo):
    for commit in RepositoryMining(f"https://github.com/{repo}.git").traverse_commits():
        if any(
            term.lower() in commit.msg.lower()
            for term in [
                "GDPR",
                "Privacy",
                "remove customer",
                "remove a customer",
                "personal data",
                "personal information",
                "anonymization",
                "anonymisation",
                "data anonymization",
                # "minimization",
                "pseudonymisation",
            ]
        ):
            yield commit


def get_all_relevant_commits():
    for repo in set(
        [
            "mirumee/saleor",
            "vuejs/vue",
            "twbs/bootstrap",
            "expressjs/express",
            "scrapy/scrapy",
            "facebook/react",
            "laravel/laravel",
            "laravel/framework",
            "moment/moment",
            "redis/redis",
            "gohugoio/hugo",
            "angular/angular",
            "rails/rails",
            "python/cpython",
            "facebook/jest",
            "jekyll/jekyll",
            "square/okhttp",
            "home-assistant/core",
            "certbot/certbot",
            "alibaba/flutter-go",
            "airbnb/lottie-web",
            "tensorflow/tensorflow",
            "django/django",
            "freeCodeCamp/freeCodeCamp",
            "shopify/shopify_api",
            "shopify/homebrew-shopify",
            "shopify/shopify_app",
            "woocommerce/woocommerce",
            "prestashop/prestashop",
            "nopSolutions/nopCommerce",
            "opencart/opencart",
            "drupal/drupal",
            "wojodesign/simplecart-js",
            "joomla/joomla-cms",
            "cubecart/v6",
            "thunder-project/thunder",
            "entynetproject/ghost",
            "intelliants/subrion",
            "textpattern/textpattern",
            "resume/resume.github.com",
            "torvalds/linux",
            "facebook/react-native",
            "electron/electron",
            "facebook/create-react-app",
            "encode/django-rest-framework",
            "prey/gdpr_rails",
            "aeris/gdpr",
            "privacyradius/gdpr-checklist",
            "privacyradius/gdpr-tracker",
            "osano/cookieconsent",
            "erichard/awesome-gdpr",
            "sander3/laravel-gdpr",
            "carhartl/jquery-cookie",
            "js-cookie/js-cookie",
            "jshttp/cookie",
            "hapijs/cookie",
            "pallets/flask",
            "microsoft/dotnet",
            "heartcombo/devise",
            "sahat/satellizer",
            "jaredhanson/passport",
            "tymondesigns/jwt-auth",
            "pennersr/django-allauth",
            "ueberauth/guardian",
            "omab/django-social-auth",
            "binarylogic/authlogic",
            "thoughtbot/clearance",
            "maxcountryman/flask-login",
            "selvin11/login",
            "braitsch/node-login",
            "therecluse26/PHP-Login",
            "BootstrapCMS/CMS",
            "lavalite/cms",
            "craftcms/cms",
            "netlify/netlify-cms",
            "cms-dev/cms",
            "overleaf/web",
            "pi-hole/web",
        ]
    ):
        try:
            print(f"\n\n\n{repo}:")
            commits = get_relevant_commits(repo)

            for commit in commits:
                yield (repo, commit)
        except Exception as e:
            print(f"Couldn't extract data from {repo} (reason: {e})")


def save_commits_to_file():
    current_time = datetime.now().strftime("%d-%m-%y-%H:%M")
    filename = f"commits_{current_time}.json"
    print(f"creating file: '{filename}'")
    commits = []
    try:
        for (repo, commit) in get_all_relevant_commits():
            commit_title = commit.msg.split("\n")[0]
            print(
                f"Message {commit_title}, author {commit.author.name}, date {commit.author_date}"
            )
            commits.append(
                {
                    "hash": commit.hash,
                    "repo": repo,
                    "date": commit.author_date.isoformat(),
                    "author": commit.author.name,
                    "msg": commit.msg,
                }
            )
    except (Exception, KeyboardInterrupt) as e:
        print(f"Processing stopped because of '{e}'")
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(commits))


if __name__ == "__main__":
    save_commits_to_file()

##[GDPR] Ability to remove a customer, author Marcin Gębala, date 2018-06-06 11:42:32+02:00

##https://github.com/freeCodeCamp/freeCodeCamp

##https://github.com/EbookFoundation/free-programming-books

##https://github.com/tensorflow/tensorflow

##https://github.com/twbs/bootstrap

##https://github.com/sindresorhus/awesome

##https://github.com/getify/You-Dont-Know-JS

##https://github.com/scrapy/scrapy
