# Python Click CLI App Example

An example of CLI app built with Python Click library.
The CLI app wraps requests to some endpoints from [FakeStore API](https://github.com/keikaavousi/fake-store-api) for demonstration purpose.

## Commands

Usage: fakecli COMMAND [OPTIONS]

### `fakecli products create`:

This command is used to add a new product with the specified attributes.

**Usage**:

```bash
fakecli products create -f file_name.json
```

**Arguments**:

- `-f <file_name.json>`: The JSON file contains the product payload.
- `-d '{"title": "Test Project"}'`: Directly pass the product payload as a string in JSON format.

### `fakecli products list`:

This command is used to get all the products.

**Usage**:

```bash
fakecli products list -o file_name
```

**Arguments**:

- `-o file_name`: Output the product list to the specified text file.

### `fakecli cart list`:

This command is used to get all the carts.

**Usage**:

```bash
fakecli cart list -o file_name
```

**Arguments**:

- `-o file_name`: Output the cart list to the specified text file.

## Features

- [x] Splitted commands
- [x] Centralized error handling
- [x] Custom validator