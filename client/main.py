import xmlrpc.client


def new(client):

    topic = input("Topic: ")
    text = input("Text: ")
    timestamp = input("Timestamp (00/00/00 - 00:00:00): ")

    client.save(topic, text, timestamp)


def fetch(client):

    topic = input("Topic: ")

    data = client.get(topic)

    print(data)


def main():

    s = xmlrpc.client.ServerProxy('http://localhost:8000')
    # Print list of available methods

    choice = input('Fetch (f)/Save (s): ')

    if choice.lower() == "f":
        fetch(s)
    else:
        new(s)


if __name__ == "__main__":
    main()
