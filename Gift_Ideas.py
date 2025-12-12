import random

# -----------------------------------------------------
# Flavor messages (adds personality!)
# -----------------------------------------------------
FLAVOR_TEXT = [
    "✨ This one always gets a great reaction.",
    "🎁 A surprisingly thoughtful pick!",
    "🔥 Top-tier gift energy right here.",
    "🌟 People LOVE receiving this!",
    "💡 Smart, stylish, and useful.",
    "😎 An underrated but amazing gift.",
    "🪄 Simple, but magical."
]


GIFTS = {
    "male": {
        "technology": [
            ("Anker 313 Power Bank (10,000mAh)", 24),
            ("Logitech MX Master 3S Mouse", 95),
            ("Sony WH-1000XM5 Headphones", 348),
            ("Apple AirTag (4 pack)", 89),
            ("RGB Desk Light Bar", 29),
            ("Raspberry Pi 5 Starter Kit", 129),
            ("Keychron K6 Mechanical Keyboard", 79),
            ("Mini 1080p Projector", 69),
            ("Samsung T7 Portable SSD 1TB", 89),
            ("Smart LED Light Strip (16ft)", 22),
            ("Bluetooth Tracking Wallet", 39),
            ("MagSafe Charger Stand", 29),
            ("LED Matrix Display Clock", 45),
            ("Portable Bluetooth Speaker (JBL Clip 4)", 49),
            ("USB Microphone (Fifine K669B)", 29),
            ("Wireless Charging Desk Pad", 32),
            ("Mechanical Numpad Add-on", 25),
        ],

        "hobbies": [
            ("Premium Leather Wallet", 45),
            ("Adjustable Dumbbell Set", 159),
            ("Whiskey Stones Gift Box", 19),
            ("Beard Grooming & Care Kit", 25),
            ("Professional Poker Set", 39),
            ("Sports Team Hoodie", 60),
            ("BBQ Stainless Grill Tool Kit", 49),
            ("LED Basketball Hoop Light", 22),
            ("Electric Screwdriver Kit", 38),
            ("Fishing Tackle Starter Set", 27),
            ("Car Detailing Kit", 32),
            ("Metal Model Puzzle Kit", 18),
            ("Mini Desk Punching Bag", 14),
            ("Beer Craft Sampler Pack", 28),
            ("Premium Sketchbook + Pencils", 21),
            ("Drone Ball (Hover Orb)", 26),
            ("Scented Car Diffuser Device", 17),
        ],

        "fashion": [
            ("Minimalist Leather Bracelet", 16),
            ("White Casual Sneakers", 55),
            ("Stainless Steel Chain Necklace", 18),
            ("Black Bomber Jacket", 45),
            ("Vintage Graphic Hoodie", 38),
            ("Aviator Sunglasses", 24),
            ("Denim Jacket (Classic Fit)", 50),
            ("Thermal Long Sleeve Set", 29),
            ("Leather Belt Premium Edition", 28),
            ("Bracelet Watch (Minimalist)", 35),
            ("Oversized Flannel Shirt", 32),
            ("Streetwear Beanie 3-Pack", 18),
        ],

        "gaming": [
            ("Steam Gift Card ($50)", 50),
            ("Xbox Wireless Controller", 64),
            ("PS5 DualSense Controller", 69),
            ("Extended RGB Mousepad", 19),
            ("HyperX Cloud II Gaming Headset", 79),
            ("LED Gaming Wall Sign", 25),
            ("Minecraft Creeper Lamp", 22),
            ("Fortnite / Apex Legends Skin Credit", 20),
            ("Retro Handheld Emulator", 40),
            ("Ergonomic Wrist Rest Set", 17),
            ("Thumb Grip Pack for Controllers", 8),
            ("Gaming Desk Cup Holder Attachment", 14),
        ]
    },

    "female": {
        "technology": [
            ("Pink Wireless Keyboard & Mouse Set", 29),
            ("Apple AirPods 3", 169),
            ("LED Vanity Mirror w/ Touch", 24),
            ("Kodak Mini Photo Printer", 79),
            ("Huion H640P Drawing Tablet", 39),
            ("Phone Tripod with Ring Light", 29),
            ("Heart-Shaped Desk Lamp (USB)", 22),
            ("Aesthetic Bluetooth Speaker Cube", 28),
            ("Smart LED Alarm Clock", 26),
            ("Wireless Charging Makeup Mirror", 31),
            ("Floral Laptop Sleeve 13-inch", 17),
            ("Colorful Cable Protectors (10 Pack)", 9),
            ("Portable Mini Desk Fan", 15),
            ("LED Display Pixel Art Cube", 55),
        ],

        "hobbies": [
            ("Luxury Spa Gift Basket", 42),
            ("Aesthetic Journal + Gold Pen Set", 18),
            ("DIY Candle-Making Kit", 35),
            ("Makeup Brush Professional Set", 27),
            ("Aesthetic Room LED Decor Kit", 25),
            ("Giant Plush (Soft & Cute)", 29),
            ("Crystal Healing Bracelet", 16),
            ("Scrapbooking Set (Cute Stickers)", 14),
            ("Adult Coloring Book + Markers", 21),
            ("Baking Essentials Starter Kit", 32),
            ("Custom Name Necklaces Kit", 20),
            ("Polaroid Photo Album Book", 16),
            ("Fluffy Lounge Socks (3-Pack)", 12),
            ("Beginner Crochet Starter Set", 18),
            ("Matcha Latte Gift Box", 27),
        ],

        "fashion": [
            ("Gold Butterfly Necklace", 12),
            ("Oversized Zip-Up Hoodie", 32),
            ("Korean-Style Canvas Tote Bag", 18),
            ("Heart-Shaped Sunglasses", 14),
            ("Crossbody Minimal Purse", 28),
            ("Layered Necklace Set (Gold)", 15),
            ("Cute Flare Sleeve Sweater", 29),
            ("Floral Summer Dress", 26),
            ("Knitted Beanie (Soft Style)", 13),
            ("Jewelry Organizer Travel Box", 19),
            ("Aesthetic Hair Clip Set", 10),
            ("Denim Jacket (Loose Fit)", 36),
        ],

        "beauty": [
            ("Perfume Rollerball Set", 22),
            ("The Ordinary Skincare Starter Kit", 29),
            ("Lip Gloss Set (Cute Colors)", 14),
            ("Ariana Grande 'Cloud' Perfume", 48),
            ("Heated Hair Styling Brush", 39),
            ("Bath Bomb 20-piece Mega Set", 20),
            ("Nail Art Decoration Kit", 17),
            ("Luxury Hand Cream Collection", 24),
            ("Face Mask Variety Box", 19),
            ("Makeup Travel Bag (Compact)", 16),
            ("Silk Sleeping Eye Mask", 13),
            ("Body Scrub Coffee Edition", 14),
        ]
    }
}


# -----------------------------------------------------
# Suggestion function
# -----------------------------------------------------
def suggest_gift(gender, category, budget):
    gender = gender.lower()
    category = category.lower()

    if gender not in GIFTS:
        return "❌ Gender must be 'male' or 'female'."

    if category not in GIFTS[gender]:
        return f"❌ Category '{category}' is not available for {gender}."

    # Filter by budget
    possible = [g for g in GIFTS[gender][category] if g[1] <= budget]

    if not possible:
        return "😕 No gifts match that budget."

    gift, price = random.choice(possible)
    flavor = random.choice(FLAVOR_TEXT)

    return f"\n🎁 **Gift Idea:** {gift}\n💰 **Price:** ${price}\n{flavor}"


# -----------------------------------------------------
# Main program
# -----------------------------------------------------
def main():
    print("\n===================================")
    print("     EXPANDED GIFT IDEAS GENERATOR")
    print("===================================")

    gender = input("Is the gift for a male or female? ").strip()

    print("\nAvailable categories:")
    print("- technology")
    print("- hobbies")
    print("- fashion")
    print("- gaming (male only)")
    print("- beauty (female only)\n")

    category = input("Choose a category: ").strip()
    budget = float(input("Max budget: $"))

    print("\n" + suggest_gift(gender, category, budget))


if __name__ == "__main__":
    main()
