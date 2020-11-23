# deps-custom-example

You can build custom deps components to automatically manage updates for custom dependency types.

This example stores the names and versions of custom dependencies in a separate YAML file,
acting like a rudimentary version of package.json.

If you have any questions (there are a number of undocumented things here!) then please [don't hestitate to ask for help or clarification](https://www.dependencies.io/contact/).

## Testing

Deps comes with a built-in testing framework.
Once you've [installed deps on your machine](https://docs.dependencies.io/local/),
you can run `deps dev test -v` while in this repo to test your component.
Note that if your test cases work by always looking for the latest version of a real dependency,
the results of the test might fail over time as new versions are published.
There are ways to avoid this,
but if you can't,
then `deps dev test --update` is your friend and will automatically update your test files!
Just be sure to double-check the output yourself before comitting it.

## Using it

You can use a custom component by putting it directly in your project:

```yaml
# deps.yml
version: 3
dependencies:
- type: ./local-custom-component
  path: example.yml
```

Or by [copying this repo template](https://github.com/dropseed/deps-custom-example/generate) and referencing it remotely (best if you're going to use it on multiple projects):

```yaml
# deps.yml
version: 3
dependencies:
- type: your-org/deps-custom-component
  path: example.yml
```
