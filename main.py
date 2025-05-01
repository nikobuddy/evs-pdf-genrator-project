import wikipedia
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Frame, Image
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
import os
import textwrap
import time
from reportlab.platypus import Image


# ---------------- CONFIG ----------------

watermark_path = "watermaeks.png"
output_folder = "evs_pdfs"
os.makedirs(output_folder, exist_ok=True)

evs_topics = [
    "Air Pollution", "Water Pollution", "Soil Pollution", "Noise Pollution", "E-Waste Management", "Plastic Pollution",
    "Climate Change", "Global Warming", "Greenhouse Effect", "Deforestation", "Urbanization", "Population Growth",
    "Ozone Layer Depletion", "Renewable Energy", "Solar Energy", "Wind Energy", "Hydroelectric Energy",
    "Nuclear Energy and Environment", "Waste Segregation", "Biodegradable vs Non-Biodegradable Waste",
    "Biodiversity Conservation", "Forest Conservation", "Wildlife Conservation", "Endangered Species",
    "Energy Conservation", "Rainwater Harvesting", "Water Conservation", "Composting", "Sustainable Development",
    "Carbon Footprint", "Green Building", "Organic Farming", "Ecotourism", "Sustainable Transportation",
    "Overfishing", "Soil Erosion", "Agroforestry", "Mangrove Ecosystems", "Reforestation", "Coral Reef Protection",
    "Marine Pollution", "Environmental Laws in India", "Ganga Action Plan", "Swachh Bharat Abhiyan",
    "Smart Cities Mission", "Natural Disasters and Environment", "Climate Refugees", "Urban Waste Management",
    "Mining and Environment", "Industrial Pollution", "Vermicomposting", "Carbon Trading"
]

styles = getSampleStyleSheet()
body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=12, leading=18, spaceAfter=12)

# ---------------- UTILITIES ----------------

def fetch_rich_wikipedia_content(topic):
    try:
        page = wikipedia.page(topic)
        content = page.content.split('\n')
        paragraphs = [para.strip() for para in content if len(para.strip()) > 80]
        full_text = " ".join(paragraphs)
        words = full_text.split()
        return " ".join(words[:3000])  # limit to ~1000+ words
    except:
        return f"Content not available for topic '{topic}'."

def create_section(title, content):
    return [Paragraph(f"<b>{title}</b>", styles['Heading1']), Spacer(1, 0.2 * inch),
            Paragraph(content, body_style), PageBreak()]

def build_pdf(topic):
    file_path = os.path.join(output_folder, f"{topic.replace(' ', '_')}.pdf")
    doc = SimpleDocTemplate(file_path, pagesize=A4, rightMargin=60, leftMargin=60, topMargin=80, bottomMargin=60)

    story = []

    # Cover page
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph(f"<b> {topic} </b>", styles['Title']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph(f"<b>Topic:</b> {topic} By Ram Lokhande", styles['Heading2']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("By: <b><i>EVS Project's PDF'S</i></b> - Download app from Play Store", styles['Normal']))
    if os.path.exists(watermark_path):
        img = Image(watermark_path, width=4*inch, height=4*inch)  # adjust size as needed
        img.hAlign = 'CENTER'
        story.append(Spacer(1, 0.5 * inch))
        story.append(img)
        story.append(PageBreak())

    # Sections
    sections = {
        "Acknowledgement": (
           f"I take this opportunity to express my profound gratitude to my respected teacher for her invaluable "
        f"guidance and encouragement throughout the completion of this EVS project on \"{topic}\". "
        f"Her constant support, feedback, and motivation have been instrumental in shaping the direction of this work.\n\n"
        f"I would also like to thank my school for providing the facilities and resources necessary to undertake this project. "
        f"This research has helped me understand the topic in depth, and its environmental implications, and has encouraged me "
        f"to think critically about sustainable solutions.\n\n"
        f"Lastly, I am grateful to my family and friends for their moral support and understanding during this endeavor. "
        f"The successful completion of this project is a result of the collective efforts and cooperation of everyone involved."
    
        ),
        "Introduction": fetch_rich_wikipedia_content(topic),
        "Types": fetch_rich_wikipedia_content(topic),
        "Case Studies": fetch_rich_wikipedia_content(topic),
        "Conclusion": (
           f"Through this project on \"{topic}\", I have learned about the various facets of environmental science and its "
        f"real-world relevance. It became evident how the topic impacts not only nature but also society, economy, and future generations.\n\n"
        f"The research revealed that while challenges exist in addressing environmental issues like {topic.lower()}, "
        f"there are also practical and innovative solutions available. It is our responsibility to adopt these solutions "
        f"and promote awareness in our communities.\n\n"
        f"In conclusion, the knowledge gained through this project has deepened my appreciation for the environment and "
        f"highlighted the importance of sustainable living. It is crucial for every individual to take active steps to "
        f"reduce their ecological footprint and work towards a greener planet."
   
        )
    }

    for sec_title, sec_content in sections.items():
        story.extend(create_section(sec_title, sec_content))

    # Build document with watermark
    def add_watermark(canvas, doc):
        if os.path.exists(watermark_path):
            canvas.saveState()
            canvas.drawImage(watermark_path, doc.pagesize[0] - 200, 20, width=160, height=160, mask='auto')
            canvas.restoreState()

    doc.build(story, onLaterPages=add_watermark, onFirstPage=add_watermark)
    print(f"✅ PDF generated: {file_path}")

# ---------------- MAIN ----------------

for topic in evs_topics:
    print(f"📘 Generating: {topic}")
    build_pdf(topic)
    time.sleep(2)
