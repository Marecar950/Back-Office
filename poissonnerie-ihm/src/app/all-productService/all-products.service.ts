import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {ProductModel} from "../model/product.model";
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class AllProductsService {

  constructor(private httClient: HttpClient) { }

  get getProducts() : Observable<ProductModel[]>  {
    return this.httClient.get<ProductModel[]>(environment.backendHost+'/getAllProducts')
  }
}
