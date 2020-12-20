"""
    Supported versions and endpoints of the Greenhouse Harvest API
"""

api_versions = {
    'v1': {
        'base': 'https://harvest.greenhouse.io/v1/',
        'uris': {
            'direct': {
                'applications': {
                    'list': 'applications',
                    'retrieve': 'applications/{id}'
                },
                'approvals': {
                    'retrieve': 'approval_flows/{id}'
                },
                'candidates': {
                    'list': 'candidates',
                    'retrieve': 'candidates/{id}'
                },
                'close_reasons': {
                    'list': 'close_reasons'
                },
                'degrees': {
                    'list': 'degrees'
                },
                'departments': {
                    'list': 'departments',
                    'retrieve': 'departments/{id}'
                },
                'disciplines': {
                    'list': 'disciplines'
                },
                'email_templates': {
                    'list': 'email_templates',
                    'retrieve': 'email_templates/{id}'
                },
                'interviews': {
                    'list': 'scheduled_interviews',
                    'retrieve': 'scheduled_interviews/{id}'
                },
                'job_posts': {
                    'list': 'job_posts',
                    'retrieve': 'job_posts/{id}'
                },
                'job_stages': {
                    'list': 'job_stages',
                    'retrieve': 'job_stages/{id}'
                },
                'jobs': {
                    'list': 'jobs',
                    'retrieve': 'jobs/{id}'
                },
                'offers': {
                    'list': 'offers',
                    'retrieve': 'offers/{id}'
                },
                'offices': {
                    'list': 'offices',
                    'retrieve': 'offices/{id}'
                },
                'prospect_pools': {
                    'list': 'prospect_pools',
                    'retrieve': 'prospect_pools/{id}'
                },
                'rejection_reasons': {
                    'list': 'rejection_reasons'
                },
                'schools': {
                    'list': 'schools'
                },
                'scorecards': {
                    'list': 'scorecards',
                    'retrieve': 'scorecards/{id}'
                },
                'sources': {
                    'list': 'sources',
                },
                'tags': {
                    'list': 'tags/candidate'
                },
                'users': {
                    'list': 'users',
                    'retrieve': 'users/{id}'
                },
                'user_roles': {
                    'list': 'user_roles',
                    'retrieve': 'user_roles/{id}'
                },
                'custom_fields': {
                    'list': 'custom_fields',
                    'retrieve': 'custom_field/{id}'
                },
            },
            'related': {
                'applications': {
                    'eeoc': {
                        'list': 'applications/{rel_id}/eeoc'
                    },
                    'interviews': {
                        'list': 'applications/{rel_id}/scheduled_interviews'
                    },
                    'offers': {
                        'list': 'applications/{rel_id}/offers'
                    },
                    'scorecards': {
                        'list': 'applications/{rel_id}/scorecards'
                    },
                },
                'candidates': {
                    'activity_feed': {
                        'list': 'candidates/{rel_id}/activity_feed'
                    },
                    'tags': {
                        'list': 'candidates/{rel_id}/tags'
                    },
                },
                'jobs': {
                    'approvals': {
                        'list': 'jobs/{rel_id}/approval_flows'
                    },
                    'hiring_team': {
                        'list': 'jobs/{rel_id}/hiring_team'
                    },
                    'openings': {
                        'list': 'jobs/{rel_id}/openings',
                        'retrieve': 'jobs/{rel_id}/openings/{{id}}'
                    },
                    'posts': {
                        'list': 'jobs/{rel_id}/job_posts',
                        'retrieve': 'jobs/{rel_id}/job_posts/{{id}}'
                    },
                    'stages': {
                        'list': 'jobs/{rel_id}/stages'
                    },
                },
                'users': {
                    'future_job_permissions': {
                        'list': 'users/{rel_id}/permissions/future_jobs'
                    },
                    'job_permissions': {
                        'list': 'users/{rel_id}/permissions/jobs'
                    },
                    'pending_approvals': {
                        'list': 'users/{rel_id}/pending_approvals'
                    },
                },
            }
        }
    }
}
