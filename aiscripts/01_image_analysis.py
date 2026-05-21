import os
import sys
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()

client = ImageAnalysisClient(
    endpoint=os.environ["AZURE_AI_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["AZURE_AI_KEY"])
)

# Imagen de ejemplo oficial de Microsoft
image_url = "https://aka.ms/azsdk/image-analysis/sample.jpg"

import sys
from pathlib import Path

if Path(sys.argv[1]).exists():
    with open(sys.argv[1], "rb") as f:
        image_data = f.read()
    result = client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE,
                VisualFeatures.READ,
                VisualFeatures.TAGS,
                VisualFeatures.SMART_CROPS,
            ],
            gender_neutral_caption=True,
            language="en",
        )
else:
    result = client.analyze_from_url(
        image_url=image_url,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.DENSE_CAPTIONS,
            VisualFeatures.OBJECTS,
            VisualFeatures.PEOPLE,
            VisualFeatures.READ,
            VisualFeatures.TAGS,
            VisualFeatures.SMART_CROPS,
        ],
        gender_neutral_caption=True,
        language="en",
    )



# Caption principal
if result.caption is not None:
    print(f"Caption: '{result.caption.text}' (confidence: {result.caption.confidence:.2%})")

# Tags
if result.tags is not None:
    print("\nTags:")
    for tag in result.tags.list:
        print(f"  - {tag.name} ({tag.confidence:.2%})")

# Objects con bounding boxes
if result.objects is not None:
    print("\nObjects:")
    for obj in result.objects.list:
        box = obj.bounding_box
        print(f"  - {obj.tags[0].name}: x={box.x}, y={box.y}, w={box.width}, h={box.height}")

# OCR (texto en la imagen)
if result.read is not None:
    print("\nText (OCR):")
    for block in result.read.blocks:
        for line in block.lines:
            print(f"  - {line.text}")
