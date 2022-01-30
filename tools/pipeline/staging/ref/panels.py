import sqlalchemy


panel = {
    'weather_precipation': {
        'filename': 'USW00023169-LAS_VEGAS_MCCARRAN_INTL_AP-precipitation-inch.csv',
        'fields': [
            {
                'column_src': 'date',
                'column_dst': 'date'
            },
            {
                'column_src': 'precipitation',
                'column_dst': 'precipitation'
            },
            {
                'column_src': 'precipitation_normal',
                'column_dst': 'precipitation_normal'
            }
        ]
    },
    'weather_temperature': {
        'filename': 'USW00023169-temperature-degreeF.csv',
        'fields': [
            {
                'column_src': 'date',
                'column_dst': 'date'
            },
            {
                'column_src': 'min',
                'column_dst': 'min'
            },
            {
                'column_src': 'max',
                'column_dst': 'max'
            },
            {
                'column_src': 'normal_min',
                'column_dst': 'normal_min'
            },
            {
                'column_src': 'normal_max',
                'column_dst': 'normal_max'
            }
        ]
    },
    'business': {
        'filename': 'yelp_academic_dataset_business.csv',
        'fields': [
            {
                'column_src': 'business_id',
                'column_dst': 'business_id'
            },
            {
                'column_src': 'name',
                'column_dst': 'business_name'
            },
            {
                'column_src': 'city',
                'column_dst': 'city'
            },
            {
                'column_src': 'state',
                'column_dst': 'state'
            }
        ]
    },
    'review': {
        'filename': 'yelp_academic_dataset_review.csv',
        'fields': [
            {
                'column_src': 'review_id',
                'column_dst': 'review_id'
            },
            {
                'column_src': 'date',
                'column_dst': 'date'
            },
            {
                'column_src': 'business_id',
                'column_dst': 'business_id'
            },
            {
                'column_src': 'stars',
                'column_dst': 'stars'
            },
            {
                'column_src': 'useful',
                'column_dst': 'useful'
            }
        ]
    }
}
