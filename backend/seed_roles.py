from app.database.session import SessionLocal

from app.models.role import Role


db = SessionLocal()

roles = [
    "Admin",
    "Analyst",
    "Manager"
]

for role_name in roles:

    role_exists = (
        db.query(Role)
        .filter(Role.name == role_name)
        .first()
    )

    if not role_exists:

        role = Role(
            name=role_name
        )

        db.add(role)

db.commit()

print("Roles Seeded Successfully")