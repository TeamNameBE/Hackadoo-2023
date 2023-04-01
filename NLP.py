
import argparse
import io
import json
import os

from google.cloud import language_v1
import numpy
import six

def classify(text, verbose=True):
    """Classify the input text into categories."""

    language_client = language_v1.LanguageServiceClient(
        client_options={
            "api_key": os.environ.get("GOOGLE_API_KEY")
        }
    )

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={"document": document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence
    print(result)

    if verbose:
        print(text)
        for category in categories:
            print("=" * 20)
            print("{:<16}: {}".format("category", category.name))

            print("{:<16}: {}".format("confidence", category.confidence))

    return result

classify("Alexios I Komnenos (Greek: Ἀλέξιος Κομνηνός, 1057 – 15 August 1118; Latinized Alexius I Comnenus) was Byzantine emperor from 1081 to 1118. Although he was not the first emperor of the Komnenian dynasty, it was during his reign that the Komnenos family came to full power and initiated a hereditary succession to the throne. Inheriting a collapsing empire and faced with constant warfare during his reign against both the Seljuq Turks in Asia Minor and the Normans in the western Balkans, Alexios was able to curb the Byzantine decline and begin the military, financial, and territorial recovery known as the Komnenian restoration. His appeals to Western Europe for help against the Turks was the catalyst that sparked the First Crusade.")