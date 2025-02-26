# Python Design Patterns

A comprehensive collection of design patterns implemented in Python to demonstrate software design principles and best practices.

## Overview

This repository serves as a learning resource for understanding and implementing common design patterns in Python. Each pattern is implemented with clear examples and explanations to help developers apply these concepts in their own projects.

## Table of Contents

- [Installation](#installation)
- [Design Pattern Categories](#design-pattern-categories)
- [Pattern Implementations](#pattern-implementations)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/zalhamami/python-design-pattern.git
cd python-design-pattern
```

No additional dependencies are required to run the examples, as they use Python's standard library.

## Design Pattern Categories

Design patterns are typically categorized into three main groups:

### 1. Creational Patterns

Patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

- [Factory Method](./creational/factory_method/)
- [Abstract Factory](./creational/abstract_factory/)
- [Builder](./creational/builder/)
- [Prototype](./creational/prototype/)
- [Singleton](./creational/singleton/)

### 2. Structural Patterns

Patterns that focus on composition of classes or objects to form larger structures.

- [Adapter](./structural/adapter/)
- [Bridge](./structural/bridge/)
- [Composite](./structural/composite/)
- [Decorator](./structural/decorator/)
- [Facade](./structural/facade/)
- [Flyweight](./structural/flyweight/)
- [Proxy](./structural/proxy/)

### 3. Behavioral Patterns

Patterns that focus on communication between objects and how responsibilities are assigned.

- [Chain of Responsibility](./behavioral/chain_of_responsibility/)
- [Command](./behavioral/command/)
- [Iterator](./behavioral/iterator/)
- [Mediator](./behavioral/mediator/)
- [Memento](./behavioral/memento/)
- [Observer](./behavioral/observer/)
- [State](./behavioral/state/)
- [Strategy](./behavioral/strategy/)
- [Template Method](./behavioral/template_method/)
- [Visitor](./behavioral/visitor/)

## Pattern Implementations

Each pattern implementation includes:

- A brief explanation of the pattern
- UML diagram where applicable
- Example code demonstrating the pattern
- Common use cases and scenarios
- Advantages and disadvantages

## Usage Examples

### Example: Singleton Pattern

```python
from creational.singleton.singleton import Singleton

# Create first instance
singleton1 = Singleton()
singleton1.value = 10

# Create second instance (should be the same object)
singleton2 = Singleton()

# Test if both variables reference the same object
print(f"Singleton1 value: {singleton1.value}")        # Output: 10
print(f"Singleton2 value: {singleton2.value}")        # Output: 10
print(f"Same instance: {singleton1 is singleton2}")   # Output: True

# Changing value in one instance affects the other
singleton2.value = 20
print(f"Singleton1 value after change: {singleton1.value}")  # Output: 20
```

### Example: Strategy Pattern

```python
from behavioral.strategy.strategy import Context, ConcreteStrategyA, ConcreteStrategyB

# Create context with strategy A
context = Context(ConcreteStrategyA())
result = context.execute_strategy()
print(f"Result with strategy A: {result}")

# Change strategy to B
context.strategy = ConcreteStrategyB()
result = context.execute_strategy()
print(f"Result with strategy B: {result}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-pattern`)
3. Commit your changes (`git commit -m 'Add some amazing pattern'`)
4. Push to the branch (`git push origin feature/amazing-pattern`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created and maintained by [zalhamami](https://github.com/zalhamami).
