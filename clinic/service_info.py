"""Text for the tap-to-open service cards and the "Common questions" section.

This is sample wording. Edit it so it matches how your clinic really works.
Each key in SERVICE_DETAILS must match a service name in site_views.py.
"""

SERVICE_DETAILS = {
    'Check-ups': {
        'included': [
            'A full physical exam: eyes, ears, teeth, heart, skin and coat',
            'Weight and body condition check',
            'Advice on food, exercise and behaviour',
        ],
        'note': 'Your vet will tell you how often your pet should come in. Puppies, kittens and older pets usually need more visits.',
    },
    'Vaccinations': {
        'included': [
            'The vaccines that suit your pet\'s species and age',
            'A vaccination record for your pet',
            'A reminder before the next dose is due',
        ],
        'note': 'Bring any earlier vaccination card so we can plan the right schedule.',
    },
    'Parasite control': {
        'included': [
            'Deworming',
            'Tick and flea prevention',
            'Advice on keeping your home and garden clear',
        ],
        'note': 'The right treatment depends on your pet\'s weight and lifestyle, so we choose it at the visit.',
    },
    'Microchipping': {
        'included': [
            'A quick chip implant under the skin',
            'Your contact details recorded in our system',
        ],
        'note': 'Keep your phone number up to date so we can reach you if a lost pet is found.',
    },
    'Illness and injury': {
        'included': [
            'Examination and diagnosis',
            'A treatment plan, with the cost explained first',
            'A follow-up check when it is needed',
        ],
        'note': 'Tell us when the problem started and any change in eating, drinking or energy.',
    },
    'Eyes and skin': {
        'included': [
            'Examination of the eyes, ears, skin and coat',
            'Tests to find the cause where needed',
            'Treatment and home-care advice',
        ],
        'note': 'Try to stop your pet rubbing or scratching the area before the visit.',
    },
    'Dental care': {
        'included': [
            'A check of the teeth and gums',
            'Cleaning where it is needed',
            'Home-care advice for fresh breath and healthy gums',
        ],
        'note': 'Bad breath, drooling or dropping food can be signs of a dental problem.',
    },
    'Laboratory tests': {
        'included': [
            'Blood, urine and stool tests',
            'Results explained in plain language',
            'Results kept in your pet\'s record',
        ],
        'note': 'Some tests need an empty stomach, so ask us when you book.',
    },
    'Surgery': {
        'included': [
            'Spaying, neutering and soft-tissue operations',
            'Pain relief and recovery advice',
            'A check-up after the operation',
        ],
        'note': 'We will tell you before the day if your pet should skip food.',
    },
    'Emergency care': {
        'included': [
            'First-aid advice by phone and how to bring your pet safely',
            'Urgent examination and treatment',
        ],
        'note': 'Call before you set off so we can get ready for you.',
    },
    'Livestock visits': {
        'included': [
            'Farm calls for cattle, goats, sheep and poultry',
            'Health checks, vaccination and treatment on site',
        ],
        'note': 'Call us to agree a day and what is needed.',
    },
}

FAQS = [
    (
        'What should I bring to my first visit?',
        'Any vaccination card or earlier records, a list of medicines your pet takes, and a lead for dogs or a carrier for cats and small animals.',
    ),
    (
        'Do I need an appointment?',
        'Booking helps us give your pet enough time, so we recommend it. You can send a request on the Book a visit page and we will call to confirm.',
    ),
    (
        'Do you treat livestock?',
        'Yes, by arrangement. Call us to agree a farm visit.',
    ),
    (
        'How much will a visit cost?',
        'It depends on the service. We explain the cost before we start any treatment.',
    ),
    (
        'What should I do in an emergency?',
        'Call us straight away, any day. We will tell you how to keep your pet calm and warm and how to bring them in.',
    ),
]
