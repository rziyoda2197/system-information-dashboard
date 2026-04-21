class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, *fields):
        self.query += "SELECT "
        self.query += ", ".join(fields)
        return self

    def from_(self, table):
        self.query += f" FROM {table}"
        return self

    def where(self, condition):
        self.query += f" WHERE {condition}"
        return self

    def and_(self, condition):
        self.query += f" AND {condition}"
        return self

    def or_(self, condition):
        self.query += f" OR {condition}"
        return self

    def group_by(self, field):
        self.query += f" GROUP BY {field}"
        return self

    def having(self, condition):
        self.query += f" HAVING {condition}"
        return self

    def order_by(self, field, direction="ASC"):
        self.query += f" ORDER BY {field} {direction}"
        return self

    def limit(self, limit):
        self.query += f" LIMIT {limit}"
        return self

    def build(self):
        return self.query


# Misol
builder = QueryBuilder()
query = (
    builder.select("id", "name", "email")
    .from_("users")
    .where("age > 18")
    .and_("country = 'USA'")
    .group_by("city")
    .having("COUNT(*) > 1")
    .order_by("name", "DESC")
    .limit(10)
    .build()
)
print(query)
```

Natija:
```sql
SELECT id, name, email FROM users WHERE age > 18 AND country = 'USA' GROUP BY city HAVING COUNT(*) > 1 ORDER BY name DESC LIMIT 10
