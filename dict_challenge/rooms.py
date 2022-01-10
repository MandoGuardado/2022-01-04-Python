rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'north' : 'Laundry Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster',
                },

            'Dining Room' : {
                'west': 'Hall',
                'south' : 'Garden',
                'north' : 'Bathroom',
                'item' : 'potion'
                },
            'Garden' : {
                'north' : 'Dining Room'
                },
            'Laundry Room' : {
                'east' : 'Bathroom',
                'south' : 'Hall',
                'item' : 'shirt'
                },
            'Bathroom' : {
                'west' : 'Laundry Room',
                'south' : 'Dining Room'
                }

         }

