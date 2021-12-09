import re
from urllib.parse import urlparse


class InfoParser:
    def __init__(self, doc) -> None:
        self.doc = doc

    def parse(self):
        info = dict()
        info_ = dict()
        for key, value in self.doc.get("info").items():
            info[key] = value
        info["url"] = self.doc.get("servers")[0].get("url")

        # check for variables in the url
        if self.doc.get("servers")[0].get("variables"):
            server = self.doc.get("servers")[0]
            for variable, variable_details in server.get("variables").items():
                info["url"] = info["url"].replace(
                    rf"{{{variable}}}", variable_details.get("default")
                )
        url = urlparse(info["url"])

        info_ = {
            "api": info.get(url.path.split("/")[0], "api"),
            "title": info.get("title", ""),
            "desc": info.get("description", ""),
            "base_url": f"{url.scheme}://{url.netloc}",
            "doc_name": info.get("", "vocab"),
        }
        info_["api"] = "{}/v{}".format(
            info_["api"], info.get("version", "1.0.0").split(".")[0]
        )
        info_["entrypoint"] = f'{info_["base_url"]}/{info_["api"]}'
        info_["id"] = f'{info_["entrypoint"]}/{info_["doc_name"]}'
        return info_
