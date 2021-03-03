import { Component, OnInit, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators, FormArray, FormControlName, Form } from '@angular/forms';
import { EdamMapService } from './edam-map/edam-map.service';
import { SpinnerService } from '../core/spinner.service';

@Component({
    selector: 'app-tool-registration',
    templateUrl: './tool-registration.component.html',
    styleUrls: ['./tool-registration.component.scss'],
    providers: [EdamMapService]
})
export class ToolRegistrationComponent implements OnInit {
    toolForm: FormGroup;

    publicationForm: FormGroup;
    publicationTypeForm: FormGroup;
    publicationTypes: string[];

    documentationForm: FormGroup;
    documentationTypeForm: FormGroup;
    documentationTypes: string[];

    downloadForm: FormGroup;
    downloadTypeForm: FormGroup;
    downloadTypes: string[];

    linkForm: FormGroup;
    linkTypeForm: FormGroup;
    linkTypes: string[];

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

        this.documentationTypes = [
            'API documentation',
            'Citation instructions',
            'Code of conduct',
            'Command-line options',
            'Contributions policy',
            'FAQ',
            'General',
            'Governance',
            'Installation instructions',
            'Quick start guide',
            'Release notes',
            'Terms of use',
            'Training material',
            'User manual',
            'Other'
        ];

        this.downloadTypes = [
            'API specification',
            'Biological data',
            'Binaries',
            'Command-line specification',
            'Container file',
            'Icon',
            'Screenshot',
            'Source code',
            'Software package',
            'Test data',
            'Test script',
            'Tool wrapper (CWL)',
            'Tool wrapper (galaxy)',
            'Tool wrapper (taverna)',
            'Tool wrapper (other)',
            'VM image',
            'Downloads page',
            'Other'
        ];

        this.linkTypes = [
            'Discussion forum',
            'Galaxy service',
            'Helpdesk',
            'Issue tracker',
            'Mailing list',
            'Mirror',
            'Software catalogue',
            'Repository',
            'Social media',
            'Service',
            'Technical monitoring',
            'Other'
        ];

        this.toolForm = this.fb.group({
            name: ['', Validators.required],
            biotoolsID: ['', Validators.required],
            homepage: ['', Validators.required],
            description: ['', Validators.required],
            // publication: this.fb.array([]),
            documentation: this.fb.array([]),
            download: this.fb.array([]),
            link: this.fb.array([])
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

    clean_tool_properties(formValue): any {
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

    // Publication

    onAddPublication(): void {
        if (!this.toolForm.get('publication')){
            this.toolForm.addControl('publication', new FormArray([]));
        }
        this.publicationForm = this.fb.group({
            doi: null,
            pmid: null,
            pmcid: null,
            type: this.fb.array([]),
            version: null,
            note: null
        });
        console.log(this.publicationForm);
        (this.toolForm.get('publication') as FormArray).push(this.publicationForm);
    }

    get publication() {
        if (this.toolForm.get('publication')){
            return (this.toolForm.get('publication') as FormArray).controls;
        }
        return null;
    }

    onPublicationTypeChange(event): any {
        const publicationTypeFormArray: FormArray = this.publicationForm.get('type') as FormArray;

        /* Selected */
        if (event.target.checked) {
            // Add a new control in the arrayForm
            publicationTypeFormArray.push(new FormControl(event.target.value));
        } else {
            // find the unselected element
            let i = 0;

            publicationTypeFormArray.controls.forEach((ctrl: FormControl) => {
                if (ctrl.value === event.target.value) {
                    // Remove the unselected element from the arrayForm
                    publicationTypeFormArray.removeAt(i);
                    return;
                }

                i++;
            });
        }
    }

    // Documentatiom
    onAddDocumentation(): void {
        this.documentationForm = this.fb.group({
            url: null,
            type: this.fb.array([]),
            note: null
        });
        console.log(this.documentationForm);
        (this.toolForm.get('documentation') as FormArray).push(this.documentationForm);
    }

    get documentation() {
        return (this.toolForm.get('documentation') as FormArray).controls;
    }

    onDocumentationTypeChange(event): any {
        const documentationTypeFormArray: FormArray = this.documentationForm.get('type') as FormArray;

        /* Selected */
        if (event.target.checked) {
            // Add a new control in the arrayForm
            documentationTypeFormArray.push(new FormControl(event.target.value));
        } else {
            // find the unselected element
            let i = 0;

            documentationTypeFormArray.controls.forEach((ctrl: FormControl) => {
                if (ctrl.value === event.target.value) {
                    // Remove the unselected element from the arrayForm
                    documentationTypeFormArray.removeAt(i);
                    return;
                }

                i++;
            });
        }
    }

    // Download
    onAddDownload(): void {
        this.downloadForm = this.fb.group({
            url: null,
            type: this.fb.array([]),
            version: null,
            note: null
        });
        console.log(this.downloadForm);
        (this.toolForm.get('download') as FormArray).push(this.downloadForm);
    }

    get download() {
        return (this.toolForm.get('download') as FormArray).controls;
    }

    onDownloadTypeChange(event): any {
        const downloadTypeFormArray: FormArray = this.downloadForm.get('type') as FormArray;

        /* Selected */
        if (event.target.checked) {
            // Add a new control in the arrayForm
            downloadTypeFormArray.push(new FormControl(event.target.value));
        } else {
            // find the unselected element
            let i = 0;

            downloadTypeFormArray.controls.forEach((ctrl: FormControl) => {
                if (ctrl.value === event.target.value) {
                    // Remove the unselected element from the arrayForm
                    downloadTypeFormArray.removeAt(i);
                    return;
                }

                i++;
            });
        }
    }

    // Links

    onAddLink(): void {
        this.linkForm = this.fb.group({
            url: null,
            type: this.fb.array([]),
            note: null
        });
        console.log(this.linkForm);
        (this.toolForm.get('link') as FormArray).push(this.linkForm);
    }

    get link() {
        return (this.toolForm.get('link') as FormArray).controls;
    }

    onLinkTypeChange(event): any {
        const linkTypeFormArray: FormArray = this.linkForm.get('type') as FormArray;

        /* Selected */
        if (event.target.checked) {
            // Add a new control in the arrayForm
            linkTypeFormArray.push(new FormControl(event.target.value));
        } else {
            // find the unselected element
            let i = 0;

            linkTypeFormArray.controls.forEach((ctrl: FormControl) => {
                if (ctrl.value === event.target.value) {
                    // Remove the unselected element from the arrayForm
                    linkTypeFormArray.removeAt(i);
                    return;
                }
                i++;
            });
        }
    }


    // EDAMmap
    onKeywordChange(e: any): void {
        this.keywords = e.target.value.trim().split(/[\r\n]+/);
    }

    prepareEDAMMapQuery(): any {
        return {
            tool: this.toolForm.value,
            keywords: this.keywords
        };
    }

    isLoading(): boolean {
        return this.spinnerService.isLoading();
    }

    private hasMinimalEDAMMapRequirements(): boolean {
        const tool = this.toolForm.value;
        if (tool.name && tool.biotoolsID && tool.homepage && tool.description) {
            return true;
        }
        alert('You need to fill in the basic information before calling EDAMmap');
        return false;
    }

    getEDAMMapTerms(): void {
        console.log(this.toolForm.value);
        if (!this.hasMinimalEDAMMapRequirements()) {
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
