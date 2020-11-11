import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators, FormArray } from '@angular/forms';
import {EdamMapService} from './edam-map/edam-map.service';

@Component({
    selector: 'app-tool-registration',
    templateUrl: './tool-registration.component.html',
    styleUrls: ['./tool-registration.component.scss'],
    providers: [EdamMapService]
})
export class ToolRegistrationComponent implements OnInit {
    toolForm: FormGroup;
    summaryForm: FormGroup;
    publicationForm: FormGroup;
    publicationTypes: string[];
    edamMapResults: any;
    constructor(private fb: FormBuilder, private edamMapService: EdamMapService) { }

    initRegistrationForm(): void {

        this.publicationTypes = [
            'Primary',
            'Benchmarking study',
            'Method',
            'Usage',
            'Review',
            'Other'
        ];
        this.publicationForm = this.fb.group({
            doi: [''],
            pmid: [''],
            pmcid: [''],
            type: ['']
        });

        this.toolForm = this.fb.group({
            name: ['', Validators.required],
            biotoolsID: ['', Validators.required],
            homepage: ['', Validators.required],
            description: ['', Validators.required],
            publication: this.fb.array([])
        });


        // this.publicationForm = new FormGroup({
        //     doi: new FormControl(null),
        //     pmid: new FormControl(null),
        //     pmcid: new FormControl(null)
        // });

        // this.toolForm = new FormGroup({
        //     name: new FormControl(null, Validators.required),
        //     biotoolsID: new FormControl(null, Validators.required),
        //     homepage: new FormControl(null, Validators.required),
        //     description: new FormControl(null, Validators.required),
        //     publication: new FormArray([])
        // });
    }

    save(): void {
        console.log(this.toolForm);
    }

    onAddPublication(): void{
        (this.toolForm.get('publication') as FormArray).push(this.publicationForm);
    }

    get publication() {
        return (this.toolForm.get('publication') as FormArray).controls;
    }

    getEDAMMapTerms(){
        console.log('Loading EDAM terms...');
        this.edamMapService.getEDAM({name: 'aTool'}).subscribe(
            (result: any) => {
                console.log(result);
            },
            (error: any) => {
                console.log(error);
            }
        );
    }

    ngOnInit(): void {
        this.initRegistrationForm();
    }

}
