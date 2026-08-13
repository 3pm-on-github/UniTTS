import requests, json

def generate(prompt: str, image: bool = False) -> str:
    if image:
        r = requests.post("https://chatbox.computer.com/api/image/prompt/1/create/", json={"prompt": prompt})
        img_r = requests.get(r.json()["image"])
        open(r.json()["image"].split("/")[-1], "wb").write(img_r.content)
        return r.json()["image"].split("/")[-1]
    else:
        r = requests.post("https://chatbox.computer.com/api/questions/1/stream/", json={"question": "answer in english: "+prompt})
        toreturn = ""
        for line in r.text.split("\n"):
            if line != "":
                toreturn += json.loads(line)["answer"]
        return toreturn