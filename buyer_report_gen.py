from fpdf import FPDF
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")


###
# Collect data from Zillow witer using requests or Python-zillow
# both requires api and web scraping doesnt works as zillow will throw unlimited captcha
###

input_property_data = ""    # Here lies the data about the location and general property data 
# Example Input 
""" Location: 110 Vandelinda Avenue, Teaneck, NJ 07666  

    Property Details:
        ●	Square Footage of Home: [3600 sq ft]
        ●	Lot Size: [8759 sq ft]
        ●	Number of Bedrooms: [6]
        ●	Number of Bathrooms: [5]
        ●	Condition of Home: [Well-maintained]
        ●	Special Features: [Patio, Outdoor Kitchen]
"""

class BuyerReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Home Purchase Pricing Report', ln=1, align='C')

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1, align='L')
        self.ln(2)

    def section_body(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, text)
        self.ln()

    def add_photo(self, photo_path, x=10, y=None, w=50):
        self.image(photo_path, x=x, y=y, w=w)
        self.ln(55)

def generate_report(output_path):
    pdf = BuyerReportPDF()
    pdf.add_page()

    # Property Overview
    pdf.section_title("Property Overview")
    #pdf.add_photo("property_image.jpg")  # Replace with actual image path
    pdf.section_body("""Address: 110 Vandelinda Avenue, Teaneck, NJ 07666
Days on Market: 40
Price History: Initially listed at $1,450,000, reduced to $1,400,000
Specifications: 6 bedrooms, 5 bathrooms, approximately 3,600 sq ft
Lot Size: 8,759 sq ft
Condition: Well-maintained with modern updates
Special Features: Large patio, landscaped backyard, outdoor kitchen
Listing Price: $1,400,000""")

    # Current Market Trends
    pdf.section_title("Current Market Trends in Teaneck, NJ")
    pdf.section_body("""The real estate market in Teaneck, NJ, has been characterized by high demand for single-family homes, particularly those with modern amenities and ample living space.
- Low Inventory: There is a limited number of high-quality homes available, leading to increased competition among buyers.
- Rising Prices: Sale prices in the area have seen steady growth, with premium properties often selling above their asking prices.
- Quick Sales: Homes in desirable neighborhoods, especially those near schools and parks, typically spend less than 60 days on the market.
- Buyer Preferences: Modernized homes with features like outdoor kitchens, finished basements, and landscaped yards are particularly sought after.""")

    # Comparable Properties (Last 6 Months)
    pdf.section_title("Comparable Properties (Last 6 Months)")
    pdf.section_body("""340 Johnson Ave, Teaneck, NJ 07666
Sale Price: $1,800,000
Days on Market: 45
Distance from Subject Property: 0.8 miles
Bedrooms/Bathrooms: 8 beds, 6 baths
Square Footage: 4,200 sq ft
Lot Size: 10,000 sq ft
Condition: Excellent, newly renovated
Special Features: Pool, tennis court
Annual Property Tax: $10,000""")
    
    # Add more properties similarly...

    # Suggested Offer Pricing Strategy
    pdf.section_title("Suggested Offer Pricing Strategy")
    pdf.section_body("""Aggressive Offer (Good for cash offer or quick close): $1,300,000
Competitive Offer (to align with market trends): $1,350,000
Maximum Offer (to secure the property): $1,400,000""")

    # Additional Considerations
    pdf.section_title("Additional Considerations")
    pdf.section_body("""- Inspection Contingency: Factor in any potential costs for updates or repairs identified during inspections.
- Appraisal: Confirm the property appraises near your offer price to avoid financing challenges.
- Market Dynamics: Stay informed about local demand trends that may influence competition.""")

    # Disclaimer
    pdf.section_title("Disclaimer")
    pdf.section_body("This report is based on publicly available data and market trends. It is intended for informational purposes only and does not constitute professional real estate advice. Buyers should consult a licensed real estate attorney or professional for specific guidance.")

    # Output the PDF
    pdf.output(output_path)
    print(f"Report saved to {output_path}")

# Generate the report
generate_report("buyer_report.pdf")
