{
  'includes': ['../../../config.gypi'],
  'targets': [
    {
      'target_name': 'binding',
      'conditions': [
         ['node_use_openssl=="true"', {
           'sources': ['binding.cc'],
           'include_dirs': ['../../../deps/openssl/openssl/include'],
           'conditions': [
              ['OS=="win"', {
	        'libraries': ['../../../../$(Configuration)/lib/<(OPENSSL_PRODUCT).lib'],
              }],
            ],
         }]
      ]
    },
  ]
}
