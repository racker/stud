{
  'targets': [
    {
      'target_name': 'stud',
      'type': 'executable',
      'dependencies': [
        'deps/uv/uv.gyp:uv',
        'deps/ebtree.gyp:ebtree',
        'deps/openssl.gyp:openssl'
      ],
      'sources': [
        'ringbuffer.c',
        'shctx.c',
        'stud.c'
      ]
    }
  ]
}
