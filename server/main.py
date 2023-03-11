from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET


tree = ET.parse('db.xml')
root = tree.getroot()

# Restrict to a particular path.


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


def get_data(topic):

    topics = [
        t
        for t in root if t.attrib["name"] == topic
    ]

    if topics:
        topic = topics[0]

        return {
            "topic": topic.attrib['name'],
            "notes": [
                {
                    "text": note.find("text").text,
                    "timestamp": note.find("timestamp").text
                }
                for note in topic
            ]

        }
    else:
        pass


# Functions


def save_data(topic, text, timestamp):

    topics = [
        t
        for t in root if t.attrib["name"] == topic
    ]

    if topics:
        topic = topics[0]

        note = ET.SubElement(topic, "note")

        text_elem = ET.SubElement(note, "text")
        text_elem.text = text

        timestamp_elem = ET.SubElement(note, "timestamp")
        timestamp_elem.text = timestamp

        tree.write("db.xml")
    else:
        # Case where topic given is not found from the database
        new_topic = ET.Element("topic")
        new_topic.attrib = {"name": topic}

        note = ET.SubElement(new_topic, "note")

        text_elem = ET.SubElement(note, "text")
        text_elem.text = text

        timestamp_elem = ET.SubElement(note, "timestamp")
        timestamp_elem.text = timestamp

        root.append(new_topic)

        tree.write("db.xml")

    return 1


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function under a different name

    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    server.register_function(save_data, "save")

    server.register_function(get_data, "get")

    # Run the server's main loop
    server.serve_forever()