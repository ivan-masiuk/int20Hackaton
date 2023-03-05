import { Box, Button, Flex, FormControl, FormLabel, Heading, Input, InputGroup, InputRightElement, Select, Stack } from '@chakra-ui/react'
import React, { useState } from 'react'

const Auth: React.FC = () => {
  const [showPassword, setShowPassword] = useState(false);

  const handleShowClick = () => setShowPassword(!showPassword);


  return (
    <Flex
      flexDirection="column"
      width="100%"
      height="calc(100vh - 72.45px)"
      justifyContent="center"
      alignItems="center"
    >
      <Stack
        flexDir="column"
        mb="2"
        spacing={12}
        justifyContent="center"
        alignItems="center"
      >
        <Heading >Знайди свою першу команду в IT</Heading>
        <Box minW={{ base: "90%", md: "468px" }}>
          <form>
            <Stack
              spacing={4}
              p="1rem"
            >
              <FormControl>
                <FormLabel>Ваш напрямок в IT</FormLabel>
                <Select>
                  <option value='option1'>Option 1</option>
                  <option value='option2'>Option 2</option>
                  <option value='option3'>Option 3</option>
                </Select>
              </FormControl>
              <FormControl>
                <FormLabel>Імʼя </FormLabel>
                <InputGroup>
                  <Input type="text" placeholder='Ваше імʼя' />
                </InputGroup>
              </FormControl>
              <FormControl>
                <FormLabel>E-mail</FormLabel>
                <InputGroup>
                  <Input placeholder='Ваш мейл' type="email" />
                </InputGroup>
              </FormControl>


              <FormControl>
                <FormLabel>Пароль</FormLabel>
                <InputGroup>
                  <Input
                    type={showPassword ? "text" : "password"}
                    placeholder="Ваш пароль"
                  />
                  <InputRightElement width="4.5rem">
                    <Button h="1.75rem" size="sm" onClick={handleShowClick}>
                      {showPassword ? "Hide" : "Show"}
                    </Button>
                  </InputRightElement>
                </InputGroup>
              </FormControl>


              <Button
                size={"lg"}
                borderRadius={8}
                type="submit"
                variant="solid"
                colorScheme="blue"
                width="full"
              >
                Зареєструватись
              </Button>
            </Stack>
          </form>
        </Box>
      </Stack>
    </Flex>
  )
}

export default Auth
