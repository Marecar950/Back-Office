import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ButtonModule} from "primeng/button";
import {StyleClassModule} from "primeng/styleclass";
import {AvatarModule} from "primeng/avatar";
import {ToolbarModule} from "primeng/toolbar";
import {DropdownModule} from "primeng/dropdown";
import {DividerModule} from "primeng/divider";
import { PoissonsComponent } from './poissons/poissons.component';
import { CrustacesComponent } from './crustaces/crustaces.component';
import { AllProductsComponent } from './all-products/all-products.component';
import { FinancesComponent } from './finances/finances.component';
import { AlertesComponent } from './alertes/alertes.component';
import { FruitDeMerComponent } from './fruit-de-mer/fruit-de-mer.component';
import { LoginComponent } from './login/login.component';
import {TableModule} from "primeng/table";
import {MultiSelectModule} from "primeng/multiselect";
import {TagModule} from "primeng/tag";
import {SliderModule} from "primeng/slider";
import {ProgressBarModule} from "primeng/progressbar";
import {ConfirmDialogModule} from "primeng/confirmdialog";
import {InputNumberModule} from "primeng/inputnumber";
import {RadioButtonModule} from "primeng/radiobutton";
import {DialogModule} from "primeng/dialog";
import {ToastModule} from "primeng/toast";
import {FileUploadModule} from "primeng/fileupload";
import {RatingModule} from "primeng/rating";
import {CheckboxModule} from "primeng/checkbox";
import {ConfirmationService, MessageService} from "primeng/api";
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    PoissonsComponent,
    CrustacesComponent,
    AllProductsComponent,
    FinancesComponent,
    AlertesComponent,
    FruitDeMerComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    StyleClassModule,
    ButtonModule,
    AvatarModule,
    ToolbarModule,
    DropdownModule,
    DividerModule,
    TableModule,
    MultiSelectModule,
    TagModule,
    SliderModule,
    ProgressBarModule,
    ConfirmDialogModule,
    InputNumberModule,
    RadioButtonModule,
    DialogModule,
    ToastModule,
    FileUploadModule,
    RatingModule,
    CheckboxModule,
    FormsModule
  ],
  providers: [
    MessageService,
    ConfirmationService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
