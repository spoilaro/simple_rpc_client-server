import xmlrpc.client


def parse_response(res):
    if res == 1:
        print("ERROR OCCURED")
        exit(1)
    else:
        return res


def new(client):

    topic = input("Topic: ")
    text = input("Text: ")
    timestamp = input("Timestamp (00/00/00 - 00:00:00): ")

    client.save(topic, text, timestamp)


def fetch(client):

    topic = input("Topic: ")

    data = parse_response(client.get(topic))

    print(data)


def wiki(client):
    topic = input("Search topic: ")

    data = parse_response(client.wiki(topic))

    print(data)


def main():

    s = xmlrpc.client.ServerProxy('http://localhost:8000')
    # Print list of available methods

    choice = input('Fetch (f)/Save (s)/ Wiki (w): ')

    if choice.lower() == "f":
        fetch(s)
    elif choice.lower() == "w":
        wiki(s)
    else:
        new(s)


if __name__ == "__main__":
    main()
