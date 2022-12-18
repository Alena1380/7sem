using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.IO;

namespace NEWTON_TASK
{
    
        public class DES
        {
            public string LastName { get; set; }
            public string FirstName { get; set; }
            public string Patronymic { get; set; }
            public DateTime BirthDate { get; set; }
            public Passportinfo PassportInfo { get; set; }
            public string INN { get; set; }
            public string SNILS { get; set; }
            public string SpecialityCode { get; set; }
            public string SpecialistName { get; set; }
            public int CourceNumber { get; set; }
            public string GroupCode { get; set; }
            public Educationalorganization EducationalOrganization { get; set; }
        }

        public class Passportinfo
        {
            public string SeriesNumber { get; set; }
            public string IssuingDepartament { get; set; }
            public DateTime Date { get; set; }
            public string DepartamentCode { get; set; }
            public Registrationadress RegistrationAdress { get; set; }
        }

        public class Registrationadress
        {
            public string Country { get; set; }
            public string Region { get; set; }
            public string City { get; set; }
            public string AddressPart { get; set; }
        }

        public class Educationalorganization
        {
            public string LegalName { get; set; }
            public string LegalAdress { get; set; }
            public string ActualAddress { get; set; }
        }
    }
