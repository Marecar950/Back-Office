export interface ProductModel {
  id: number,
  name: string,
  price: number,
  unit: string,
  availability: boolean,
  sale: boolean,
  discount: number,
  pourcentage_promo: number,
  quantite_stock: number,
  nombre_articles_vendus: number,
  comments: string,
  category: number
}
