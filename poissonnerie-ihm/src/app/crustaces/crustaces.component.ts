import {Component, OnInit, ViewChild} from '@angular/core';
import {Table} from "primeng/table";
import {ProductModel} from "../model/product.model";
import {AllProductsService} from "../all-productService/all-products.service";
import {ConfirmationService, MessageService} from "primeng/api";

@Component({
  selector: 'app-crustaces',
  templateUrl: './crustaces.component.html',
  styleUrls: ['./crustaces.component.css']
})
export class CrustacesComponent implements OnInit{
  @ViewChild('dt', { static: true }) dt!: Table;
  productDialog: boolean = false;

  products!: ProductModel[];

  //product: ProductModel = {};
  product: Partial<ProductModel> = {}

  selectedProducts!: ProductModel[] | null;

  submitted: boolean = false;

  statuses!: any[];
  Delete: any;

  // constructor(private productService: AllProductsService, private messageService: MessageService, private confirmationService: ConfirmationService) {}

  constructor(private productService: AllProductsService, private messageService: MessageService,private confirmationService: ConfirmationService){}
  ngOnInit() {

    this.productService.getProducts.subscribe(data=> {
      this.products = data.filter(product => product.category === 1);
      console.log(data)
    })

    this.statuses = [
      { label: 'INSTOCK', value: 'instock' },
      { label: 'LOWSTOCK', value: 'lowstock' },
      { label: 'OUTOFSTOCK', value: 'outofstock' }
    ];
  }



  getSeverity(status: string): string {
    switch (status) {
      case 'INSTOCK':
        return 'success';
      case 'LOWSTOCK':
        return 'warning';
      case 'OUTOFSTOCK':
        return 'danger';
      default:
        return ''; // Ajout d'un cas de retour par défaut
    }
  }

  sendStockChange(product: any) {

  }

  sendDataToBackend() {

  }
}
