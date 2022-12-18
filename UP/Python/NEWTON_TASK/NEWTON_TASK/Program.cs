using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;

namespace NEWTON_TASK
{
    internal class Program
    {
        static void Main(string[] args)
        {

            new JSONPARSE().Provide(out DES DESObject);
            DES sad = DESObject;
            Console.WriteLine(sad.LastName);
            Console.WriteLine(sad.FirstName);
            Console.WriteLine(sad.Patronymic);
            Console.WriteLine(sad.BirthDate);
            Console.WriteLine(sad.PassportInfo);
            Console.WriteLine(sad.INN);
            Console.WriteLine(sad.SNILS);
            Console.WriteLine(sad.SpecialityCode);
            Console.WriteLine(sad.SpecialistName);
            Console.WriteLine(sad.CourceNumber);
            Console.WriteLine(sad.GroupCode);
            Console.WriteLine(sad.EducationalOrganization);
        }
    }
}
