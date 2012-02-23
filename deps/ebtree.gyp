{
  'targets': [
    {
      'target_name': 'ebtree',
      'type': 'static_library',
      'include_dirs': ['ebtree'],
      'direct_dependent_settings': {
        'include_dirs': ['.']
      },
      'sources': [
        'ebtree/ebistree.c',
        'ebtree/ebimtree.c',
        'ebtree/ebsttree.c',
        'ebtree/ebmbtree.c',
        'ebtree/eb64tree.c',
        'ebtree/eb32tree.c',
        'ebtree/ebtree.c'
      ]
    }
  ]
}
