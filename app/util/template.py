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

DAILY_NUTRITION = {
    'mom': {
        'triwulan 1': """
          Energi (kkal): 2330
          Protein (g): 61
          Lemak Total (g): 62.3
          Omega 3 (g): 1.4
          Omega 6 (g): 14
          Karbohidrat (g): 365
          Serat (g): 33
          Air (ml): 2650
          Vit A (RE): 900
          Vit D (mcg): 15
          Vit E (mcg): 15
          Vit K (mcg): 55
          Vit B1 (mg): 1.4
          Vit B2 (mg): 1.4
          Vit B3 (mg): 18
          Vit B5 (Pantotenat) (mg): 6.0
          Vit B6 (mg): 1.9
          Folat (mcg): 600
          Vit B12 (mcg): 4.5
          Biotin (mcg): 30
          Kolin (mg): 450
          Vit C (mg): 85
          Kalsium (mg): 1200
          Fosfor (mg): 700
          Magnesium (mg): 340
          Besi (mg): 18
          Iodium (mcg): 220
          Seng (mg): 10
          Selenium (mcg): 30
          Mangan (mg): 2
          Fluor (mg): 3.0
          Kromium (mcg): 34
          Kalium (mg): 4700
          Natrium (mg): 1500
          Klor (mg): 2250
          Tembaga (mcg): 1000
        """,
        'triwulan 2': """
          Energi (kkal): 2450
          Protein (g): 70
          Lemak Total (g): 62.3
          Omega 3 (g): 1.4
          Omega 6 (g): 14
          Karbohidrat (g): 380
          Serat (g): 34
          Air (ml): 2650
          Vit A (RE): 900
          Vit D (mcg): 15
          Vit E (mcg): 15
          Vit K (mcg): 55
          Vit B1 (mg): 1.4
          Vit B2 (mg): 1.4
          Vit B3 (mg): 18
          Vit B5 (Pantotenat) (mg): 6.0
          Vit B6 (mg): 1.9
          Folat (mcg): 600
          Vit B12 (mcg): 4.5
          Biotin (mcg): 30
          Kolin (mg): 450
          Vit C (mg): 85
          Kalsium (mg): 1200
          Fosfor (mg): 700
          Magnesium (mg): 340
          Besi (mg): 27
          Iodium (mcg): 220
          Seng (mg): 12
          Selenium (mcg): 30
          Mangan (mg): 2
          Fluor (mg): 3.0
          Kromium (mcg): 34
          Kalium (mg): 4700
          Natrium (mg): 1500
          Klor (mg): 2250
          Tembaga (mcg): 1000
        """,
        'triwulan 3': """
          Energi (kkal): 2450
          Protein (g): 90
          Lemak Total (g): 62.3
          Omega 3 (g): 1.4
          Omega 6 (g): 14
          Karbohidrat (g): 380
          Serat (g): 34
          Air (ml): 2650
          Vit A (RE): 900
          Vit D (mcg): 15
          Vit E (mcg): 15
          Vit K (mcg): 55
          Vit B1 (mg): 1.4
          Vit B2 (mg): 1.4
          Vit B3 (mg): 18
          Vit B5 (Pantotenat) (mg): 6.0
          Vit B6 (mg): 1.9
          Folat (mcg): 600
          Vit B12 (mcg): 4.5
          Biotin (mcg): 30
          Kolin (mg): 450
          Vit C (mg): 85
          Kalsium (mg): 1200
          Fosfor (mg): 700
          Magnesium (mg): 340
          Besi (mg): 27
          Iodium (mcg): 220
          Seng (mg): 12
          Selenium (mcg): 30
          Mangan (mg): 2
          Fluor (mg): 3.0
          Kromium (mcg): 34
          Kalium (mg): 4700
          Natrium (mg): 1500
          Klor (mg): 2250
          Tembaga (mcg): 1000
        """,
    },
    'baby': {
        '0-5 bulan': """
          Energi (kkal): 550
          Protein (g): 9
          Lemak Total (g): 31
          Omega 3 (g): 0.5
          Omega 6 (g): 4.4
          Karbohidrat (g): 59
          Serat (g): 0
          Air (ml): 700
          Vit A (RE): 375
          Vit D (mcg): 10
          Vit E (mcg): 4
          Vit K (mcg): 5
          Vit B1 (mg): 0.2
          Vit B2 (mg): 0.3
          Vit B3 (mg): 2
          Vit B5 (Pantotenat) (mg): 1.7
          Vit B6 (mg): 0.1
          Folat (mcg): 80
          Vit B12 (mcg): 0.4
          Biotin (mcg): 5
          Kolin (mg): 125
          Vit C (mg): 40
          Kalsium (mg): 200
          Fosfor (mg): 100
          Magnesium (mg): 30
          Besi (mg): 0.3
          Iodium (mcg): 90
          Seng (mg): 1.1
          Selenium (mcg): 7
          Mangan (mg): 0.003
          Fluor (mg): 0.01
          Kromium (mcg): 0.2
          Kalium (mg): 400
          Natrium (mg): 120
          Klor (mg): 180
          Tembaga (mcg): 200
        """,
        '6-11 bulan': """
          Energi (kkal): 800
          Protein (g): 15
          Lemak Total (g): 35
          Omega 3 (g): 0.5
          Omega 6 (g): 4.4
          Karbohidrat (g): 105
          Serat (g): 11
          Air (ml): 900
          Vit A (RE): 400
          Vit D (mcg): 10
          Vit E (mcg): 5
          Vit K (mcg): 10
          Vit B1 (mg): 0.3
          Vit B2 (mg): 0.4
          Vit B3 (mg): 4
          Vit B5 (Pantotenat) (mg): 1.8
          Vit B6 (mg): 0.3
          Folat (mcg): 80
          Vit B12 (mcg): 1.5
          Biotin (mcg): 6
          Kolin (mg): 150
          Vit C (mg): 50
          Kalsium (mg): 270
          Fosfor (mg): 275
          Magnesium (mg): 55
          Besi (mg): 11
          Iodium (mcg): 120
          Seng (mg): 3
          Selenium (mcg): 10
          Mangan (mg): 0.7
          Fluor (mg): 0.5
          Kromium (mcg): 6
          Kalium (mg): 700
          Natrium (mg): 370
          Klor (mg): 570
          Tembaga (mcg): 220
        """,
        '1-3 tahun': """
          Energi (kkal): 1350
          Protein (g): 20
          Lemak Total (g): 45
          Omega 3 (g): 0.7
          Omega 6 (g): 7
          Karbohidrat (g): 215
          Serat (g): 19
          Air (ml): 1150
          Vit A (RE): 400
          Vit D (mcg): 15
          Vit E (mcg): 6
          Vit K (mcg): 15
          Vit B1 (mg): 0.5
          Vit B2 (mg): 0.5
          Vit B3 (mg): 6
          Vit B5 (Pantotenat) (mg): 2.0
          Vit B6 (mg): 0.5
          Folat (mcg): 160
          Vit B12 (mcg): 1.5
          Biotin (mcg): 8
          Kolin (mg): 200
          Vit C (mg): 40
          Kalsium (mg): 650
          Fosfor (mg): 460
          Magnesium (mg): 65
          Besi (mg): 7
          Iodium (mcg): 90
          Seng (mg): 3
          Selenium (mcg): 18
          Mangan (mg): 1.2
          Fluor (mg): 0.7
          Kromium (mcg): 14
          Kalium (mg): 2600
          Natrium (mg): 800
          Klor (mg): 1200
          Tembaga (mcg): 340
        """
    }
}