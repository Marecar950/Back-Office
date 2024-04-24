import {Component, OnInit, ViewChild} from '@angular/core';
import {ProductModel} from "../model/product.model";
import {ConfirmationService, MessageService} from "primeng/api";
import {AllProductsService} from "../all-productService/all-products.service";
import {Table} from "primeng/table";

@Component({
  selector: 'app-all-products',
  templateUrl: './all-products.component.html',
  styleUrls: ['./all-products.component.scss']
})
export class AllProductsComponent implements OnInit{
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
      this.products = data
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
