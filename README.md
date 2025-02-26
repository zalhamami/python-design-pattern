# Python Design Patterns

A comprehensive collection of design patterns implemented in Python to demonstrate software design principles and best practices.

## Overview

This repository provides practical implementations of classic design patterns in Python. Each pattern is implemented as a standalone example file, making it easy to understand and apply these concepts in your own projects.

## Design Pattern Categories

The repository is organized based on the three main categories of design patterns:

### 1. Creational Patterns

Patterns that deal with object creation mechanisms:

- [Abstract Factory](./creational/abstract_factory.py) - Provides an interface for creating families of related objects
- [Builder](./creational/builder.py) - Separates object construction from its representation
- [Factory](./creational/factory.py) - Creates objects without specifying the exact class to create
- [Prototype](./creational/prototype.py) - Creates new objects by copying existing ones
- [Singleton](./creational/singleton.py) - Ensures a class has only one instance

### 2. Structural Patterns

Patterns that focus on object composition:

- [Adapter](./structural/adapter.py) - Allows incompatible interfaces to work together
- [Bridge](./structural/bridge.py) - Separates an abstraction from its implementation
- [Composite](./structural/composite.py) - Composes objects into tree structures
- [Decorator](./structural/decorator.py) - Adds responsibilities to objects dynamically
- [Proxy](./structural/proxy.py) - Provides a surrogate for another object

### 3. Behavioral Patterns

Patterns that focus on communication between objects:

- [Chain of Responsibility](./behavioural/chain.py) - Passes requests along a chain of handlers
- [Iterator](./behavioural/iterator.py) - Accesses elements of a collection sequentially
- [Observer](./behavioural/observer.py) - Defines a one-to-many dependency between objects
- [Strategy](./behavioural/strategy.py) - Defines a family of algorithms and makes them interchangeable
- [Visitor](./behavioural/visitor.py) - Separates algorithms from the objects on which they operate

## Usage Examples

### Example: Singleton Pattern

```python
# Import the Singleton class
# You can directly use the singleton.py file

# First instance
singleton1 = Singleton()
singleton1.value = 10

# Second instance (same object)
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
# Import from strategy.py
# context = Context()
# context.set_strategy(ConcreteStrategyA())
# result = context.execute_strategy()
```

## Learning Resources

Each pattern file includes:
- Brief explanation of the pattern
- Implementation example
- Use cases when the pattern is applicable

## Contributing

Contributions are welcome! If you'd like to add new patterns or improve existing ones:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-pattern`)
3. Commit your changes (`git commit -m 'Add some pattern'`)
4. Push to the branch (`git push origin feature/new-pattern`)
5. Open a Pull Request

---

Created and maintained by [zalhamami](https://github.com/zalhamami).
