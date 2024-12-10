food_json_schema = {
    "title": "foods",
    "description": "Contain all details of food",
    "type": "array",
    "items": [
        {
            "title": "nutrition of foods",
            "description": "Describe the food nutritions",
            "type": "object",
            "properties": {
                "energi": {
                  "title": "Energi (kkal)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Energy in kkal (kilocalories)"
                },
                "protein": {
                  "title": "Protein (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Protein in grams (g)"
                },
                "lemak_total": {
                  "title": "Lemak Total (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Total fat in grams (g)"
                },
                "omega_3": {
                  "title": "Omega 3 (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Omega-3 in grams (g)"
                },
                "omega_6": {
                  "title": "Omega 6 (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Omega-6 in grams (g)"
                },
                "karbohidrat": {
                  "title": "Karbohidrat (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Carbohydrate in grams (g)"
                },
                "serat": {
                  "title": "Serat (g)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Fiber in grams (g)"
                },
                "air": {
                  "title": "Air (ml)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Water in milliliters (ml)"
                },
                "vit_a": {
                  "title": "Vit A (RE)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin A in milligrams (mg)"
                },
                "vit_d": {
                  "title": "Vit D (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin D in milligrams (mg)"
                },
                "vit_e": {
                  "title": "Vit E (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin E in milligrams (mg)"
                },
                "vit_k": {
                  "title": "Vit K (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin K in milligrams (mg)"
                },
                "vit_b1": {
                  "title": "Vit B1 (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B1 in milligrams (mg)"
                },
                "vit_b2": {
                  "title": "Vit B2 (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B2 in milligrams (mg)"
                },
                "vit_b3": {
                  "title": "Vit B3 (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B3 in milligrams (mg)"
                },
                "vit_b5": {
                  "title": "Vit B5 (Pantotenat) (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B5 in milligrams (mg)"
                },
                "vit_b6": {
                  "title": "Vit B6 (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B6 in milligrams (mg)"
                },
                "folat": {
                  "title": "Folat (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Folate in milligrams (mg)"
                },
                "vit_b12": {
                  "title": "Vit B12 (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin B12 in milligrams (mg)"
                },
                "biotin": {
                  "title": "Biotin (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Biotin in milligrams (mg)"
                },
                "kolin": {
                  "title": "Kolin (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Coilin in milligrams (mg)"
                },
                "vit_c": {
                  "title": "Vit C (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Vitamin C in milligrams (mg)"
                },
                "kalsium": {
                  "title": "Kalsium (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Calcium in milligrams (mg)"
                },
                "fosfor": {
                  "title": "Fosfor (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Phosphorus in milligrams (mg)"
                },
                "magnesium": {
                  "title": "Magnesium (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Magnesium in milligrams (mg)"
                },
                "besi": {
                  "title": "Besi (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Iron in milligrams (mg)"
                },
                "iodium": {
                  "title": "Iodium (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Iodine in milligrams (mg)"
                },
                "seng": {
                  "title": "Seng (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Manganese in milligrams (mg)"
                },
                "selenium": {
                  "title": "Selenium (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Selenium in milligrams (mg)"
                },
                "mangan": {
                  "title": "Mangan (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Molybdenum in milligrams (mg)"
                },
                "fluor": {
                  "title": "Fluor (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Fluorine in milligrams (mg)"
                },
                "kromium": {
                  "title": "Kromium (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Chromium in milligrams (mg)"
                },
                "kalium": {
                  "title": "Kalium (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Potassium in milligrams (mg)"
                },
                "natrium": {
                  "title": "Natrium (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Sodium in milligrams (mg)"
                },
                "klor": {
                  "title": "Klor (mg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Chloride in milligrams (mg)"
                },
                "tembaga": {
                  "title": "Tembaga (mcg)",
                  "type": "number",
                  "multipleOf" : 0.01,
                  "description": "Zinc in milligrams (mg)"
                },
            },
            # "required": ['energi', 'protein', 'lemak_total', 'omega_3', 'omega_6', 'karbohidrat', 'serat', 'air', 'vit_a', 'vit_d', 'vit_e', 'vit_k', 'vit_b1', 'vit_b2', 'vit_b3', 'vit_b5', 'vit_b6', 'folat', 'vit_b12', 'biotin', 'kolin', 'vit_c', 'kalsium', 'fosfor', 'magnesium', 'besi', 'iodium', 'seng', 'selenium', 'mangan', 'fluor', 'kromium', 'kalium', 'natrium', 'klor', 'tembaga'],
        },
    ],
}

EXAMPLE_STRUCTURE_RESPONSE = """
{
        "foods": [
          {
              'nama_makanan': 'Nasi goreng',
              'jumlah_porsi': 1,
              'nutrition': {
                'energi': 120.00,
                'protein': 20.00,
                'lemak_total': 5.20,
                'omega_3': 0.32,
                'omega_6': 0.12,
                'karbohidrat': 150.21,
                'serat': 10.00,
                'air': 2.00,
                'vit_a': 0.22,
                'vit_d': 0.12,
                'vit_e': 0.02,
                'vit_k': 0.01,
                'vit_b1': 0.02,
                'vit_b2': 0.02,
                'vit_b3': 0.01,
                'vit_b5': 0.00,
                'vit_b6': 0.00,
                'folat': 0.00,
                'vit_b12': 0.00,
                'biotin': 0.00,
                'kolin': 0.00,
                'vit_c': 0.00,
                'kalsium': 0.00,
                'fosfor': 0.00,
                'magnesium': 0.00,
                'besi': 0.01,
                'iodium': 0.02,
                'seng': 0.01,
                'selenium': 0.01,
                'mangan': 0.01,
                'fluor': 0.02,
                'kromium': 0.02,
                'kalium': 0.01,
                'natrium': 0.01,
                'klor': 0.02,
                'tembaga': 0.01
              }
          }
        ]
      }
"""