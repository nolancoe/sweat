module.exports = {
  root: true,
  extends: 'airbnb-base',
  env: {
    browser: true,
  },
  rules: {
    'import/no-extraneous-dependencies': 'off',
    'no-param-reassign': 'off',
    'no-restricted-properties': 'off',
    'valid-jsdoc': ['error', {
      requireReturn: false,
    }],
  },
  overrides: [
    {
      files: 'test/**/*.spec.js',
      env: {
        mocha: true,
      },
      globals: {
        Cropper: true,
        expect: true,
      },
      rules: {
        'no-new': 'off',
        'no-unused-expressions': 'off',
      },
    },
  ],
};
