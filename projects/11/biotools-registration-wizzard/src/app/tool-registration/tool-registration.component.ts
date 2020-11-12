import { Component, OnInit, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators, FormArray, FormControlName } from '@angular/forms';
import { EdamMapService } from './edam-map/edam-map.service';
import {SpinnerService} from '../core/spinner.service';

@Component({
    selector: 'app-tool-registration',
    templateUrl: './tool-registration.component.html',
    styleUrls: ['./tool-registration.component.scss'],
    providers: [EdamMapService]
})
export class ToolRegistrationComponent implements OnInit {
    toolForm: FormGroup;
    publicationForm: FormGroup;
    publicationTypes: string[];

    keywords: string;

    edamMapError: string;
    edamMapResults: any;
    constructor(
        private fb: FormBuilder,
        private edamMapService: EdamMapService,
        private spinnerService: SpinnerService
    ) { }

    initRegistrationForm(): void {

        this.publicationTypes = [
            'Primary',
            'Benchmarking study',
            'Method',
            'Usage',
            'Review',
            'Other'
        ];

        this.toolForm = this.fb.group({
            name: ['', Validators.required],
            biotoolsID: ['', Validators.required],
            homepage: ['', Validators.required],
            description: ['', Validators.required],
            publication: this.fb.array([])
        });

        this.edamMapError = null;
        this.edamMapResults = null;

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

    clean_tool_properties(formValue): any{
        // Will need to improve this, doen't clean an object if all its fields are null
        // see https://stackoverflow.com/questions/40770425/tslint-codelyzer-ng-lint-error-for-in-statements-must-be-filtere
        // tslint:disable-next-line: forin
        for (const prop in formValue) {
            if (!formValue[prop]) {
                delete formValue[prop];
            }

            if (Array.isArray(formValue[prop])) {
                const resultArray = formValue[prop].filter(item => item);
                if (resultArray.length > 0) {
                    formValue[prop] = resultArray;
                } else {
                    delete formValue[prop];
                }
            }
        }

        return formValue;
    }

    save(): void {

        const toolValue = this.clean_tool_properties(this.toolForm.value);
        console.log(toolValue);
    }

    onAddPublication(): void {
        this.publicationForm = this.fb.group({
            doi: null,
            pmid: null,
            pmcid: null,
            type: null
        });
        console.log(this.publicationForm);
        (this.toolForm.get('publication') as FormArray).push(this.publicationForm);
    }

    get publication() {
        return (this.toolForm.get('publication') as FormArray).controls;
    }


    onKeywordChange(e: any): void {
        this.keywords = e.target.value.trim().split(/[\r\n]+/);
    }

    prepareEDAMMapQuery(): any {
        return  {
            tool: this.toolForm.value,
            keywords: this.keywords
        };
    }

    isLoading(): boolean{
        return this.spinnerService.isLoading();
    }

    private hasMinimalEDAMMapRequirements(): boolean{
        const tool = this.toolForm.value;
        if (tool.name && tool.biotoolsID && tool.homepage && tool.description){
            return true;
        }
        alert('You need to fill in the basic information before calling EDAMmap');
        return false;
    }

    getEDAMMapTerms(): void {
        console.log(this.toolForm.value);
        if (!this.hasMinimalEDAMMapRequirements()){
            return;
        }
        this.spinnerService.show();
        const edamMapQuery = this.prepareEDAMMapQuery();
        console.log('Loading EDAM terms...');
        this.edamMapService.getEDAM(edamMapQuery).subscribe(
            (result: any) => {
                console.log(result);
                this.edamMapResults = result;
                this.spinnerService.hide();
            },
            (error: any) => {
                this.edamMapError = error.error.message;
                this.spinnerService.hide();
            }
        );
    }

    ngOnInit(): void {
        this.initRegistrationForm();
    }

}
