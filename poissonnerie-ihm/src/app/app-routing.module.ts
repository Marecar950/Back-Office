import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PoissonsComponent} from "./poissons/poissons.component";
import {CrustacesComponent} from "./crustaces/crustaces.component";
import {FruitDeMerComponent} from "./fruit-de-mer/fruit-de-mer.component";
import {FinancesComponent} from "./finances/finances.component";
import {AlertesComponent} from "./alertes/alertes.component";
import {AllProductsComponent} from "./all-products/all-products.component";

const routes: Routes = [
  {path: "poissons", component: PoissonsComponent},
  {path: "crustaces", component: CrustacesComponent},
  {path: "fruitdemers", component: FruitDeMerComponent},
  {path: "produits", component: AllProductsComponent},
  {path: "finances", component: FinancesComponent},
  {path: "alertes", component: AlertesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
