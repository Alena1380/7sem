using System.IO;
using System.Text.Json;
namespace NEWTON_TASK
{
    internal class JSONPARSE
    {
        private const string _nameJsonFile = "responce.json";
        public void Provide(out DES DESObject)
        {
            string objectJsonFile =  File.ReadAllText(_nameJsonFile);
            DESObject = JsonSerializer.Deserialize<DES>(objectJsonFile);
        }
    }
}
