from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.product import Base, Product
from repository.product_repository import ProductRepository


def main():
    engine = create_engine(
        "postgresql+psycopg2://postgres:admin@localhost:5432/shopdb",
        future=True,
        echo=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine, future=True)
    session = Session()

    repo = ProductRepository(session)

    # Création d’un produit
    prod = Product(name="Mangue", category="Fruit", price=1.99, stock_quantity=20)
    repo.add(prod)

    # Récupération du produit
    fetched = repo.get_by_id(prod.id)
    print("Produit récupéré:", fetched)

    # Liste de tous les produits
    all_products = repo.get_all()
    print("Tous les produits:", all_products)


if __name__ == "__main__":
    main()
